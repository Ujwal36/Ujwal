import weakref
from unittest.mock import Mock, call, patch

import pytest

from bl.executor.load_generators.local_load_generator import LocalLoadGenerator
from bl.executor.result import Result
from test_framework.assertions import PjacError


def test_local_load_generator():
    class TestMock(Mock):
        def __init__(self, result):
            super().__init__()
            _result = lambda: None  # noqa: E731
            _result.get_result = lambda: result
            self.result = _result

    tests = [TestMock(Result.Error), TestMock(Result.Failure), TestMock(Result.Skip), TestMock(Result.Success)]
    workers = Mock()
    main_loop = Mock()
    test_factory = Mock(side_effect=tests)
    load_generator = Mock()

    local_load_generator = LocalLoadGenerator(workers=workers,
                                              main_loop=main_loop,
                                              test_factory=test_factory,
                                              testcases=['T-1', 'T-2'],
                                              repeat_count=2,
                                              load_generator=load_generator)

    assert local_load_generator.total_count == len(tests)
    assert local_load_generator.finished_count == 0
    assert sorted(local_load_generator.testcases) == ['T-1', 'T-1', 'T-2', 'T-2']
    test_factory.assert_has_calls(
        [call(arguments=None, load_generator=weakref.proxy(local_load_generator), testcase_id='T-2'),
         call(arguments=None, load_generator=weakref.proxy(local_load_generator), testcase_id='T-2'),
         call(arguments=None, load_generator=weakref.proxy(local_load_generator), testcase_id='T-1'),
         call(arguments=None, load_generator=weakref.proxy(local_load_generator), testcase_id='T-1')],
        any_order=True)

    workers.push.assert_has_calls([call(test) for test in tests], any_order=True)
    for test in tests:
        test.on_finished(test)

    assert local_load_generator.finished_count == len(tests)
    main_loop.stop.assert_called()


def test_local_load_generator_repeat_count():
    local = LocalLoadGenerator(workers=Mock(),
                               main_loop=Mock(),
                               test_factory=Mock(),
                               testcases=['T-1', 'T-2', 'T-3', 'T-4'],
                               repeat_count=2,
                               load_generator=Mock())
    assert sorted(local.testcases) == ['T-1', 'T-1', 'T-2', 'T-2', 'T-3', 'T-3', 'T-4', 'T-4']


@patch('bl.executor.load_generators.local_load_generator.context')
@patch('bl.executor.load_generators.local_load_generator.Settings')
def test_preserve_order_single_work_thread(settings_mock, context_mock):
    """Tests when "shuffle_tests" resource parameter is set to "False" and workers count equal to 1."""

    def side_effect(name, with_type, **kwargs):
        settings = {'shuffle_tests': False, 'skip_tests': ''}
        return settings.get(name)

    settings_mock.get.side_effect = side_effect
    context_mock().arguments.work_threads = 1
    testcases = ['T-3', 'T-1', 'T-2']
    local_load_generator = LocalLoadGenerator(workers=Mock(),
                                              main_loop=Mock(),
                                              test_factory=Mock(),
                                              testcases=testcases,
                                              repeat_count=1,
                                              load_generator=Mock())
    assert local_load_generator.testcases == testcases


@patch('bl.executor.load_generators.local_load_generator.context')
@patch('bl.executor.load_generators.local_load_generator.Settings')
def test_preserve_order_multiple_work_threads(settings_mock, context_mock):
    """Tests when "shuffle_tests" resource parameter is set to "False" and workers count is not equal to 1."""

    def side_effect(name, with_type, **kwargs):
        settings = {'shuffle_tests': False, 'skip_tests': ''}
        return settings.get(name)

    settings_mock.get.side_effect = side_effect
    context_mock().arguments.work_threads = 2
    with pytest.raises(PjacError) as error:
        LocalLoadGenerator(workers=Mock(),
                           main_loop=Mock(),
                           test_factory=Mock(),
                           testcases=['T-3', 'T-1', 'T-2'],
                           repeat_count=1,
                           load_generator=Mock())
    assert error.value.message == 'Tests with preserved order executed in one thread'
