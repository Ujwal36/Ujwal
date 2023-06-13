"""This module contains unit tests for PDV load generator."""
import json
from unittest.mock import MagicMock, Mock, mock_open, patch

import pytest
from wheezy.core.collections import attrdict

import bl.executor.load_generators.views.pdv as pdv_views
from bl.executor.load_generators.pdv_load_generator import PdvLoadGenerator


@pytest.fixture(scope='module')
def pdv_load_generator():
    """PDV load generator fixture."""
    load_generator = PdvLoadGenerator(test_factory=MagicMock(), workers=MagicMock(), load_generator=MagicMock())
    load_generator.running_tests = MagicMock()
    yield load_generator
    load_generator.stop()


def test_pdv_load_generator_actions(pdv_load_generator, request_mock):
    """Tests handling of actions request in pdv load generator."""
    pdv_load_generator.test_factory.return_value = Mock(run_id='test-0', state='NOT_STARTED', result='')
    pdv_load_generator.load_generator.address = 'address'

    request_body = {'testcase_id': 'TBB-1'}
    actions_request = request_mock(method='POST', body=request_body)
    route_args = {'route_args': {'pdv_load_generator': pdv_load_generator}}
    actions_request.environ.update(route_args)
    actions_response = pdv_views.ActionsHandler(actions_request)
    assert actions_response.status_code == 201
    response_data = {'result': 'OK', 'status_url': 'actions/test-0', 'report_url': 'actions/test-0/report'}
    assert actions_response.buffer[0].decode() == json.dumps(response_data, separators=(',', ':'))


def test_pdv_load_generator_action(pdv_load_generator, request_mock):
    """Tests handling of action request in pdv load generator."""
    test = Mock(run_id='test-0', state='FINISHED')
    test.result.result = Mock(console_format='PASS')

    pdv_load_generator.running_tests.get.return_value = test
    action_request = request_mock(method='GET', body={})
    route_args = {'route_args': attrdict(pdv_load_generator=pdv_load_generator, action_id='test-0')}
    action_request.environ.update(route_args)
    action_response = pdv_views.ActionHandler(action_request)
    assert action_response.status_code == 200
    response_data = {'result': 'OK', 'status': 'PASS'}
    assert action_response.buffer[0].decode() == json.dumps(response_data, separators=(',', ':'))


def test_pdv_load_generator_actions_report(pdv_load_generator, request_mock):
    """Tests handling of actions report request in pdv load generator."""
    test = Mock(run_id='test-0', state='FINISHED')
    test.result.result = Mock(console_format='PASS')

    pdv_load_generator.running_tests.get.return_value = test
    report_request = request_mock(method='GET', body={})
    route_args = {'route_args': attrdict(pdv_load_generator=pdv_load_generator, action_id='test-0')}
    report_request.environ.update(route_args)
    with patch('builtins.open', mock_open(read_data='report')):
        report_response = pdv_views.ReportHandler(report_request)
        assert report_response.status_code == 200
        assert report_response.buffer[0].decode() == 'report'
