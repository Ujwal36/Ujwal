"""This module contains unit tests for account collector load generator."""
import json
import time
from unittest.mock import patch

import pytest

import bl.executor.load_generators.views.account_collector as account_collector_views
from bl.executor.load_generators.tests.helpers import update_load_generator_storage
from test_framework.assertions import PjacAssertion
from test_framework.common.timer import Timer
from test_framework.helpers import current_file_path_join
from test_framework.paths import Paths
from test_framework.settings import SettingFoundError, Settings

TEST_SETS_PARAMETERS = (
    ('unittests_data', {'test_sets': []}),
    ('assets', {'test_sets': [{'name': 'set.csv', 'type': 'csv'}]})
)


@patch('test_framework.testcase.arguments.Settings')
def test_account_collector_load_generator_post_test_names_normal_case(settings_mock,
                                                                      account_collector_load_generator,
                                                                      request_mock):
    """Tests handling of POST test names request in service load generator."""

    settings_mock.get = lambda name: {'ibo_country_p0': 'USA,GBR'}[name]

    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))

    # test normal case (`200 OK`)
    request_body = {
        'testnames': ['test1', 'test2'],
        'params': []
    }
    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    response = account_collector_views.TestNamesHandler(request)
    testnames = [
        'test1',
        'test2(ibo_country_p0=USA)',
        'test2(ibo_country_p0=GBR)'
    ]
    expected_response_data = {'testnames': testnames}
    assert response.status_code == 200
    assert response.buffer[0].decode() == json.dumps(expected_response_data, separators=(',', ':'))


@patch('test_framework.testcase.arguments.Settings')
def test_account_collector_load_generator_post_test_names_not_found_case(lg_settings_mock,
                                                                         account_collector_load_generator,
                                                                         request_mock):
    """Tests handling not found case of POST test names request in service load generator."""

    settings_storage = {'ibo_country_p0': 'USA,GBR'}

    def settings_mock_storage_update(overrides):
        settings_storage.update(overrides)

    lg_settings_mock.storage().update = settings_mock_storage_update

    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))

    # test error case (`404 Not Found`)
    request_body = {
        'testnames': ['test1', 'TBB-fake0', 'TBB-fake1'],
        'params': []
    }
    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    response = account_collector_views.TestNamesHandler(request)

    expected_response_data = {
        'reason': 'missing_testcases',
        'missing_testcases': ['TBB-fake0', 'TBB-fake1']
    }

    assert response.status_code == 404
    assert response.buffer[0].decode() == json.dumps(expected_response_data, separators=(',', ':'))


@patch('test_framework.testcase.arguments.Settings')
@patch('test_framework.settings.Settings')
def test_account_collector_load_generator_post_test_names_bad_request_case(lg_settings_mock, settings_mock,
                                                                           account_collector_load_generator,
                                                                           request_mock):
    """Tests handling bad request case of POST test names request in service load generator."""

    settings_storage = {'ibo_country_p0': 'USA,GBR'}

    def settings_mock_get(name):
        element = settings_storage.get(name)
        if element:
            return element
        raise SettingFoundError(name)

    def settings_mock_storage_update(overrides):
        settings_storage.update(overrides)

    settings_mock.get = settings_mock_get
    settings_mock.Sip_OutboundPstnProxy = 5001
    lg_settings_mock.storage().update = settings_mock_storage_update

    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))

    # test error case (`400 Bad Request`)
    request_body = {
        'testnames': ['test3'],
        'params': []
    }
    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    response = account_collector_views.TestNamesHandler(request)
    expected_response_data = {
        'reason': 'missing_params',
        'missing_params': ['fake_param']
    }

    assert response.status_code == 400
    assert response.buffer[0].decode() == json.dumps(expected_response_data, separators=(',', ':'))


@patch('test_framework.testcase.arguments.Settings')
@patch('bl.phone_numbers.Settings')
def test_post_test_names_returns_all_testcases(phone_settings_mock,
                                               settings_mock,
                                               account_collector_load_generator,
                                               request_mock):
    """Tests POST /testnames returns all possible testcases when "testnames" field in empty."""

    settings_storage = {'ibo_country_p0': 'USA,GBR', 'fake_param': 'dummy'}
    settings_mock.get = lambda name: settings_storage[name]
    phone_settings_mock.Sip_OutboundPstnProxy = 5001

    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))

    request_body = {
        'testnames': [],
        'params': []
    }
    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    response = account_collector_views.TestNamesHandler(request)
    testnames = [
        'test1',
        'test2(ibo_country_p0=USA)',
        'test2(ibo_country_p0=GBR)',
        'test3(fake_param=dummy)',
        'test4',
        'test5',
        'test6',
        'test7'
    ]
    expected_response_data = {'testnames': testnames}
    assert response.status_code == 200
    assert response.buffer[0].decode() == json.dumps(expected_response_data, separators=(',', ':'))


@patch('test_framework.testcase.arguments.Settings')
@patch('bl.phone_numbers.Settings')
def test_account_collector_load_generator_post_test_info_normal_case(phone_settings_mock, settings_mock,
                                                                     account_collector_load_generator,
                                                                     request_mock):
    """Tests handling of POST test info request in account collector load generator."""

    settings_mock.get = lambda name: {'ibo_country_p0': 'USA,GBR'}[name]
    phone_settings_mock.Sip_OutboundPstnProxy = 5001

    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))

    request_body = {
        'testcases': [
            'test5'
        ],
        'params': [],
        'resources': []
    }

    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    response = account_collector_views.TestInfoHandler(request)
    expected_response_data = {
        'complete': True,
        'accountmap': {
            'test5': {
                'complete': True,
                'bound': False,
                'accounts': [
                    'TBB.CISCO.POLYCOM.HD'
                ]
            }
        }
    }

    assert response.status_code == 200
    assert response.buffer[0].decode() == json.dumps(expected_response_data, separators=(',', ':'))


@patch('test_framework.testcase.arguments.Settings')
def test_account_collector_load_generator_post_test_info_templates(settings_mock,
                                                                   account_collector_load_generator,
                                                                   request_mock):
    """Tests account collection is complete when tests with recursive accounts use templates in scenario names."""
    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))

    request_body = {
        'testcases': ['test4', 'test5']
    }

    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    response = account_collector_views.TestInfoHandler(request)
    expected_response_data = {
        'complete': True,
        'accountmap': {
            'test4': {
                'complete': True,
                'bound': False,
                'accounts': [
                    '<ref=account2>SCENARIO2',
                    'SCENARIO1(forwarding_number=<link=account2, fn=digital_lines.find_by_pin(\"105\").first()>)'
                ]
            },
            'test5': {
                'complete': True,
                'bound': False,
                'accounts': [
                    'TBB.CISCO.POLYCOM.HD'
                ]
            }
        }
    }

    assert response.status_code == 200
    assert response.buffer[0].decode() == json.dumps(expected_response_data, separators=(',', ':'))


@patch('test_framework.testcase.arguments.Settings')
def test_account_collector_load_generator_post_test_info_complete_false(settings_mock,
                                                                        account_collector_load_generator,
                                                                        request_mock):
    """Tests exception is raised when test with recursive accounts does not use templates in scenario names."""
    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))

    request_body = {
        'testcases': ['test7']
    }

    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    with pytest.raises(PjacAssertion):
        account_collector_views.TestInfoHandler(request)


def test_account_collector_load_generator_post_test_info_no_accounts(account_collector_load_generator, request_mock):
    """Tests POST /testinfo returns empty account map for tests with @no_accounts."""
    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))

    request_body = {
        'testcases': [
            'test6'
        ],
        'params': [],
        'resources': []
    }

    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    response = account_collector_views.TestInfoHandler(request)
    expected_response_data = {
        'complete': True,
        'accountmap': {'test6': {'complete': True, "bound": False, "accounts": []}}
    }

    assert response.status_code == 200
    assert response.buffer[0].decode() == json.dumps(expected_response_data, separators=(',', ':'))


@pytest.mark.parametrize('directory,expected_data', TEST_SETS_PARAMETERS)
def test_account_collector_generator_test_sets(directory, expected_data, request_mock):
    """Tests /testsets endpoint of account collector generator."""
    with patch('bl.executor.load_generators.views.account_collector.Paths') as paths_mock:
        paths_mock.sets.return_value = current_file_path_join(__file__, directory)
        request = request_mock(method='GET', body={})
        response = account_collector_views.TestSets(request)

    assert response.status_code == 200
    assert response.buffer[0].decode() == json.dumps(expected_data, separators=(',', ':'))


@pytest.mark.integration_test
def test_account_collector_load_generator_all_accounts(account_collector_load_generator, request_mock):
    """Tests POST /testinfo for all testcases."""
    Settings.load(environment_name='FTI-CI-AMS')

    update_load_generator_storage(account_collector_load_generator, Paths.testcases())

    request_body = {
        'testcases': [],
    }

    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    timer = Timer(600)
    while not timer.fired():
        response = account_collector_views.TestInfoHandler(request)
        assert response.status_code in (200, 202)
        if response.status_code == 202:
            time.sleep(5)
        else:
            break
    assert timer.remainder() > 0
    exception = json.loads(response.buffer[0].decode()).get('exception')
    assert exception is None


def test_testinfo_not_found_configured_using_request_parameter(account_collector_load_generator, request_mock):
    """Tests POST /testinfo returns 200 and missing testcases info when parameter is specified in request data."""
    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))

    request_body = {
        'testcases': [
            'TBB-DOESNOTEXIST1',
            'test5',
            'TBB-DOESNOTEXIST2'
        ],
        'params': ['accounts_collector_require_existing_testcases=false'],
    }
    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)
    response = account_collector_views.TestInfoHandler(request)

    expected = {
        'complete': True,
        'accountmap': {
            'test5': {
                'complete': True,
                'bound': False,
                'accounts': [
                    'TBB.CISCO.POLYCOM.HD'
                ]
            }
        },
        'missing_testcases': ['TBB-DOESNOTEXIST1', 'TBB-DOESNOTEXIST2']
    }
    assert response.status_code == 200
    assert response.buffer[0].decode() == json.dumps(expected, separators=(',', ':'))


@patch('bl.executor.load_generators.views.account_collector.Settings')
def test_testinfo_not_found_configured_using_settings(settings_mock, account_collector_load_generator, request_mock):
    """Tests POST /testinfo returns 200 and missing testcases info when setting is set."""
    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))
    settings = {'accounts_collector_require_existing_testcases': False}
    settings_mock.get = lambda name, with_type, default: settings[name]

    request_body = {
        'testcases': [
            'TBB-DOESNOTEXIST1',
            'test5',
            'TBB-DOESNOTEXIST2'
        ],
    }
    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)
    response = account_collector_views.TestInfoHandler(request)

    expected = {
        'complete': True,
        'accountmap': {
            'test5': {
                'complete': True,
                'bound': False,
                'accounts': [
                    'TBB.CISCO.POLYCOM.HD'
                ]
            }
        },
        'missing_testcases': ['TBB-DOESNOTEXIST1', 'TBB-DOESNOTEXIST2']
    }
    assert response.status_code == 200
    assert response.buffer[0].decode() == json.dumps(expected, separators=(',', ':'))


def test_testnames_not_found_configured_using_request_parameter(account_collector_load_generator, request_mock):
    """Tests POST /testnames returns 200 and missing testcases info when parameter is specified in request data."""
    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))

    request_body = {
        'testnames': ['TBB-DOESNOTEXIST1', 'test1', 'TBB-DOESNOTEXIST2'],
        'params': ['accounts_collector_require_existing_testcases=false']
    }
    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    response = account_collector_views.TestNamesHandler(request)
    expected = {
        'testnames': ['test1'],
        'missing_testcases': ['TBB-DOESNOTEXIST1', 'TBB-DOESNOTEXIST2']
    }
    assert response.status_code == 200
    assert response.buffer[0].decode() == json.dumps(expected, separators=(',', ':'))


@patch('bl.executor.load_generators.views.account_collector.Settings')
def test_testnames_not_found_configured_using_settings(settings_mock, account_collector_load_generator, request_mock):
    """Tests POST /testnames returns 200 and missing testcases info when setting is set."""
    update_load_generator_storage(account_collector_load_generator, current_file_path_join(__file__, 'unittests_data'))
    settings = {'accounts_collector_require_existing_testcases': False}
    settings_mock.get = lambda name, with_type, default: settings[name]

    request_body = {
        'testnames': ['TBB-DOESNOTEXIST1', 'test1', 'TBB-DOESNOTEXIST2']
    }
    request = request_mock(method='POST', body=request_body)

    route_args = {'route_args': {'account_collector_load_generator': account_collector_load_generator}}
    request.environ.update(route_args)

    response = account_collector_views.TestNamesHandler(request)
    expected = {
        'testnames': ['test1'],
        'missing_testcases': ['TBB-DOESNOTEXIST1', 'TBB-DOESNOTEXIST2']
    }
    assert response.status_code == 200
    assert response.buffer[0].decode() == json.dumps(expected, separators=(',', ':'))
