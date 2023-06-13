"""This module contains unit tests for stress load generator."""
from unittest.mock import Mock, patch

import pytest

from bl.executor.load_generators.stress_load_generator import StressLoadGenerator
from bl.executor.load_generators.views.stress import (GetStatusHandler, RunTestsHandler, SetThreadsHandler,
                                                      StopTestsHandler)


@pytest.fixture(scope='module')
def stress_load_generator():
    """Stress load generator fixture."""
    with patch('bl.executor.load_generators.stress_load_generator.Stresser'):
        stress_generator = StressLoadGenerator(test_factory=Mock(), workers=Mock(), load_generator=Mock())
    yield stress_generator
    stress_generator.stop()


def test_stress_load_generator_run_tests(stress_load_generator, request_mock):
    """Tests handling of run tests request in stress load generator."""
    request_body = {
        'run_id': 1,
        'threads': 20,
        'testcases': [
            {'id': 'TBB-1', 'percent': 10},
            {'id': 'TBB-2', 'percent': 40},
            {'id': 'TBB-3', 'percent': 50}
        ]
    }
    run_test_request = request_mock(method='POST', body=request_body)
    route_args = {'route_args': {'stress_load_generator': stress_load_generator}}
    run_test_request.environ.update(route_args)
    run_response = RunTestsHandler(run_test_request)
    assert run_response.status_code == 200
    assert run_response.buffer[0].decode() == '{"result":"ok"}'
    test_case_percents = [('TBB-1', 10), ('TBB-2', 40), ('TBB-3', 50)]
    stresser = stress_load_generator.stresser
    stresser.run_tests.assert_called_with(run_id=1, testcases_percents=test_case_percents, threads=20)


def test_stress_load_generator_set_threads(stress_load_generator, request_mock):
    """Tests handling of set threads request in stress load generator."""
    set_threads_request = request_mock(method='PATCH', body={'threads': 30})
    route_args = {'route_args': {'stress_load_generator': stress_load_generator}}
    set_threads_request.environ.update(route_args)
    set_threads_response = SetThreadsHandler(set_threads_request)
    assert set_threads_response.status_code == 200
    assert set_threads_response.buffer[0].decode() == '{"result":"ok"}'
    stresser = stress_load_generator.stresser
    stresser.set_threads.assert_called_with(30)


def test_stress_load_generator_stop_tests(stress_load_generator, request_mock):
    """Tests handling of stop tests request in stress load generator."""
    stop_tests_request = request_mock(method='GET', body={})
    route_args = {'route_args': {'stress_load_generator': stress_load_generator}}
    stop_tests_request.environ.update(route_args)
    stop_tests_response = StopTestsHandler(stop_tests_request)
    assert stop_tests_response.status_code == 200
    assert stop_tests_response.buffer[0].decode() == '{"result":"ok"}'
    stresser = stress_load_generator.stresser
    stresser.stop_tests.assert_called()


def test_stress_load_generator_get_status(stress_load_generator, request_mock):
    """Tests handling of get status request in stress load generator."""
    stress_load_generator.stresser.get_status = Mock(return_value=('Running', 123, 20))
    get_status_request = request_mock(method='GET', body={})
    route_args = {'route_args': {'stress_load_generator': stress_load_generator}}
    get_status_request.environ.update(route_args)
    get_status_response = GetStatusHandler(get_status_request)
    assert get_status_response.status_code == 200
    response_data = '{"result":"ok","status":"Running","run_seconds":123,"threads":20}'
    assert get_status_response.buffer[0].decode() == response_data
