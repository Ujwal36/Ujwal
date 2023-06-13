"""This module contains unit tests for load generators and views helpers."""
import collections

import pytest

from bl.executor.load_generators.helpers import split_tests_string
from bl.executor.load_generators.views.helpers import get_prepared_accounts_data


def test_get_prepared_accounts_data_no_tests():
    """Tests receipt of prepared accounts data when provided tests are empty."""
    assert get_prepared_accounts_data({}) == collections.defaultdict(list)


def test_get_prepared_accounts_data_no_resources(runs_post_request_valid):
    """Tests receipt of prepared accounts data when request has no "resources" field."""
    tests = runs_post_request_valid['tests']
    del tests[0]['resources']
    test = tests[0]
    assert get_prepared_accounts_data(test) == collections.defaultdict(list)


def test_get_prepared_accounts_data_no_ready_accounts(runs_post_request_valid):
    """Tests receipt of prepared accounts data when request has no "ready accounts" resouces field."""
    tests = runs_post_request_valid['tests']
    del tests[0]['resources'][0]['type']
    test = tests[0]
    assert get_prepared_accounts_data(test) == collections.defaultdict(list)


def test_get_prepared_accounts_data_no_data(runs_post_request_valid):
    """Tests receipt of prepared accounts data when request has no "data" in resouces field."""
    tests = runs_post_request_valid['tests']
    del tests[0]['resources'][0]['data']
    test = tests[0]
    assert get_prepared_accounts_data(test) == collections.defaultdict(list)


def test_get_prepared_accounts_data_no_accounts(runs_post_request_valid):
    """Tests receipt of prepared accounts data when request has no "accounts" in data field."""
    tests = runs_post_request_valid['tests']
    del tests[0]['resources'][0]['data']['accounts']
    test = tests[0]
    assert get_prepared_accounts_data(test) == collections.defaultdict(list)


def test_get_prepared_accounts_data_accounts_exist(runs_post_request_valid):
    """Tests receipt of prepared accounts data when data is present."""
    prepared_accounts_data = {
        "AGS.PSTN_HOLDER": ["_ACCOUNT_JSON_FROM_AGS_"],
        "AGS.4U.4HP.4SP": ["_ACCOUNT_JSON_FROM_AGS_"]
    }
    expected_data = collections.defaultdict(list, prepared_accounts_data)
    test = runs_post_request_valid['tests'][0]
    assert get_prepared_accounts_data(test) == expected_data


def test_testcase_split():
    """Tests split tests helper function."""
    assert split_tests_string('') == []

    with pytest.raises(TypeError):
        split_tests_string(1)

    assert split_tests_string('T-1') == ['T-1']
    assert split_tests_string('T-1,T-2;T-3(x=0) T-4') == ['T-1', 'T-2', 'T-3(x=0)', 'T-4']
