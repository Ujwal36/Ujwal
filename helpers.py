"""This module contains helper functions for load generator unit tests."""
from test_framework.testcase.testcase_storage import TestCaseStorage


def update_load_generator_storage(load_generator, tests):
    """Updates test factory's storage of load generator with tests.

    :param test_framework.common.web_server.base.app.BaseWebApp load_generator: Load generator.
    :param tests: Absolute path to directory with tests.

    :return: None
    """
    storage = TestCaseStorage.instance()
    storage.collect_tests(tests)
    load_generator.test_factory.storage = storage
