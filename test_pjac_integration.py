"""This module contains integrations tests for PJAC in service and account collector modes."""

import os
import re
import subprocess
from collections import namedtuple
from queue import Empty, Queue
from threading import Thread
from time import sleep

import pytest

from bl.http_client import HttpClient
from test_framework.common.timer import Timer
from test_framework.paths import Paths

PjacArgs = namedtuple(
    'PjacArgs',
    [
        'environment',
        'help',
        'mode',
        'param',
        'release_clean',
        'repeat',
        'run',
        'setting',
        'subset',
        'testcases',
        'trace_enable',
        'work_threads',
        'workspace'
    ]
)


def enqueue_output(out, queue):
    """Put line to the queue"""
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()


def read_line(lines_queue) -> str:
    """Non block read from queue with stdout lines"""
    try:
        line = lines_queue.get_nowait()
    except Empty:
        return ''
    return line.decode()


def _wait_pjac_web_service_started(q) -> str:
    """Waits for the PJAC web service to start"""
    timer = Timer(50)
    while not timer.fired():
        data = read_line(q)
        res = re.search(r'Web service is waiting requests on (http://\S+:\d+)', data)
        if res:
            url = res.group(1)
            return url
        sleep(min(timer.remainder(), 2))
    return ''


TEST_ACCOUNTS = [{
    'AGS.TAF.ICDR_1': {
        'id': 6332738, 'rcUserId': 759945053, 'mainPhoneNumber': '+18557095556',
        'password': 'Test!123', 'signupCoockie': None, 'tierId': 4513, 'brandId': 1210,
        'offerTypeId': None, 'durationTypeId': None, 'sysMailboxId': 759945053,
        'status': 'CLEAN', 'scenario': 'AGS.TAF.ICDR_1', 'subset': 'service', 'jobId': 7556935,
        'partnerId': None, 'externalBillingId': '',
        'mailboxes': [
            {'id': 10014245, 'rcMailboxId': 759945053, 'pin': '101', 'firstName': 'Something',
             'lastName': 'New', 'email': 'mm1+2175502@stressmail.lab.nordigy.ru', 'password': 'Test!123',
             'ivrPin': '3569975425', 'extensionTypeId': 1, 'accessLevelId': 666},
            {'id': 10014246, 'rcMailboxId': 759947053, 'pin': '102', 'firstName': 'DLOP',
             'lastName': 'User_102', 'email': 'mm1+2182842@stressmail.lab.nordigy.ru', 'password': 'Test!123',
             'ivrPin': '3569975425', 'extensionTypeId': 1, 'accessLevelId': 999}],
        'phoneNumbers': [
            {'id': 12003312, 'mailboxId': 759947053, 'rcPhoneNumberId': 335864053, 'paymentTypeId': 6,
             'areaCode': None, 'phoneNumber': '+15302834444', 'phoneTypeId': 2, 'vanityNumber': None,
             'label': 'ext 102'},
            {'id': 12003313, 'mailboxId': 759945053, 'rcPhoneNumberId': 335862053, 'paymentTypeId': 5,
             'areaCode': None, 'phoneNumber': '+18557095556', 'phoneTypeId': 2, 'vanityNumber': None,
             'label': 'MainNumber'},
            {'id': 12003311, 'mailboxId': 759945053, 'rcPhoneNumberId': 335863053, 'paymentTypeId': 6,
             'areaCode': None, 'phoneNumber': '+15302875555', 'phoneTypeId': 2, 'vanityNumber': None,
             'label': 'ext 101'}
        ], 'forwardingNumbers': [
            {'id': 4942074, 'mailboxId': 759945053, 'rcForwardNumberId': 548550053,
             'phoneNumber': '+15302875555', 'codec': None, 'label': 'DL_1'},
            {'id': 4942075, 'mailboxId': 759947053, 'rcForwardNumberId': 548551053,
             'phoneNumber': '+15302834444', 'codec': None, 'label': 'DL_2'}
        ], 'digitalLines': [
            {'phoneNumberId': 335863053, 'rcDigitalLineId': 69295053, 'defaultAreaCode': None,
             'deviceTypeId': 0, 'serial': 'HELL82920053-759945053', 'codec': None,
             'authorizationId': '82920053', 'password': 's4wjgLHa2O', 'label': 'DL_1',
             'deviceInstanceId': 82920053},
            {'phoneNumberId': 335864053, 'rcDigitalLineId': 69296053, 'defaultAreaCode': None,
             'deviceTypeId': 0, 'serial': 'HELL82921053-759945053', 'codec': None,
             'authorizationId': '82921053', 'password': 'F4mMuBy', 'label': 'DL_2',
             'deviceInstanceId': 82921053}
        ], 'devices': [
            {'id': 7276304, 'rcInstanceId': 82920053, 'deviceTypeId': 0, 'codec': None, 'label': 'DL_1',
             'serial': 'HELL82920053-759945053', 'username': '15302875555', 'password': 's4wjgLHa2O',
             'authorizationId': '82920053', 'domain': 'sip-fticiams.lab.nordigy.ru',
             'outboundProxy': 'sip-fticiams.lab.nordigy.ru:5090'},
            {'id': 7276305, 'rcInstanceId': 82921053, 'deviceTypeId': 0, 'codec': None, 'label': 'DL_2',
             'serial': 'HELL82921053-759945053', 'username': '15302834444', 'password': 'F4mMuBy',
             'authorizationId': '82921053', 'domain': 'sip-fticiams.lab.nordigy.ru',
             'outboundProxy': 'sip-fticiams.lab.nordigy.ru:5090'}
        ]
    }
}, {
    'AGS.TAF.ICDR_1': {
        'id': 6332759, 'rcUserId': 759948053, 'mainPhoneNumber': '+18332251304',
        'password': 'Test!123', 'signupCoockie': None, 'tierId': 4513, 'brandId': 1210,
        'offerTypeId': None, 'durationTypeId': None, 'sysMailboxId': 759948053,
        'status': 'CLEAN', 'scenario': 'AGS.TAF.ICDR_1', 'subset': 'service', 'jobId': 7556979,
        'partnerId': None, 'externalBillingId': '',
        'mailboxes': [
            {'id': 10014277, 'rcMailboxId': 759948053, 'pin': '101', 'firstName': 'Something',
             'lastName': 'New', 'email': 'mm1+1879715@stressmail.lab.nordigy.ru', 'password': 'Test!123',
             'ivrPin': '3569975425', 'extensionTypeId': 1, 'accessLevelId': 666},
            {'id': 10014278, 'rcMailboxId': 759950053, 'pin': '102', 'firstName': 'DLOP',
             'lastName': 'User_102', 'email': 'mm1+5202196@stressmail.lab.nordigy.ru', 'password': 'Test!123',
             'ivrPin': '3569975425', 'extensionTypeId': 1, 'accessLevelId': 999}
        ],
        'phoneNumbers': [
            {'id': 12003352, 'mailboxId': 759948053, 'rcPhoneNumberId': 335866053, 'paymentTypeId': 6,
             'areaCode': None, 'phoneNumber': '+15303021111', 'phoneTypeId': 2, 'vanityNumber': None,
             'label': 'ext 101'},
            {'id': 12003353, 'mailboxId': 759950053, 'rcPhoneNumberId': 335867053, 'paymentTypeId': 6,
             'areaCode': None, 'phoneNumber': '+15302741111', 'phoneTypeId': 2, 'vanityNumber': None,
             'label': 'ext 102'},
            {'id': 12003354, 'mailboxId': 759948053, 'rcPhoneNumberId': 335865053, 'paymentTypeId': 5,
             'areaCode': None, 'phoneNumber': '+18332251304', 'phoneTypeId': 2, 'vanityNumber': None,
             'label': 'MainNumber'}
        ],
        'forwardingNumbers': [
            {'id': 4942100, 'mailboxId': 759948053, 'rcForwardNumberId': 548555053,
             'phoneNumber': '+15303021111', 'codec': None, 'label': 'DL_1'},
            {'id': 4942101, 'mailboxId': 759950053, 'rcForwardNumberId': 548556053,
             'phoneNumber': '+15302741111', 'codec': None, 'label': 'DL_2'}
        ],
        'digitalLines': [
            {'phoneNumberId': 335866053, 'rcDigitalLineId': 69297053, 'defaultAreaCode': None,
             'deviceTypeId': 0, 'serial': 'HELL82922053-759948053', 'codec': None,
             'authorizationId': '82922053', 'password': 's68VVX4', 'label': 'DL_1',
             'deviceInstanceId': 82922053},
            {'phoneNumberId': 335867053, 'rcDigitalLineId': 69298053, 'defaultAreaCode': None,
             'deviceTypeId': 0, 'serial': 'HELL82923053-759948053', 'codec': None,
             'authorizationId': '82923053', 'password': 'K8y4r5', 'label': 'DL_2',
             'deviceInstanceId': 82923053}
        ],
        'devices': [
            {'id': 7276331, 'rcInstanceId': 82922053, 'deviceTypeId': 0, 'codec': None, 'label': 'DL_1',
             'serial': 'HELL82922053-759948053', 'username': '15303021111', 'password': 's68VVX4',
             'authorizationId': '82922053', 'domain': 'sip-fticiams.lab.nordigy.ru',
             'outboundProxy': 'sip-fticiams.lab.nordigy.ru:5090'},
            {'id': 7276332, 'rcInstanceId': 82923053, 'deviceTypeId': 0, 'codec': None, 'label': 'DL_2',
             'serial': 'HELL82923053-759948053', 'username': '15302741111', 'password': 'K8y4r5',
             'authorizationId': '82923053', 'domain': 'sip-fticiams.lab.nordigy.ru',
             'outboundProxy': 'sip-fticiams.lab.nordigy.ru:5090'}
        ]
    }
}]


@pytest.fixture(scope='function')
def pjac_process(pjac_args: PjacArgs):
    """Start PJAC process"""
    proc = subprocess.Popen(
        [
            'python', os.path.join(Paths.pjac_fw(), 'run.py'),
            '-n', pjac_args.environment,
            '-m', pjac_args.mode,
            '-P', *(f'{k}={v}' for k, v in pjac_args.param.items()),
            '-r', str(pjac_args.repeat),
            '-u', str(pjac_args.run),
            '-w', str(pjac_args.work_threads),
            '-o', pjac_args.workspace,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    lines_queue = Queue()
    thread = Thread(target=enqueue_output, args=(proc.stdout, lines_queue), daemon=True)
    thread.start()
    yield {'proc': proc, 'lines_queue': lines_queue}
    proc.terminate()


@pytest.mark.integration_test
@pytest.mark.parametrize('pjac_args', [PjacArgs(
    environment='DEV-AUT-AMS',
    help=False,
    mode='service',
    param={'warmup_speed': 6000000},  # warmup delay = 60 / 6000000 * 10 = 0.0001 s
    release_clean=False,
    repeat=1,
    run=1,
    setting='',
    subset='',
    testcases='',
    trace_enable=False,
    work_threads=10,
    workspace=Paths.workspace()
)])
def test_pjac_in_service_mode(pjac_process, pjac_args):
    """Test PJAC in service mode"""
    url = _wait_pjac_web_service_started(pjac_process['lines_queue'])
    assert url, 'Web service URL not found in process output'

    client = HttpClient(url=url)

    # check that all workers are ready
    r = client.get('runstatus')
    expected_response_data = {
        'status': 'pending',
        'free_test_slots': 10
    }
    assert r.status_code == 200
    assert r.json() == expected_response_data

    # run tests
    request_body = {
        'run_id': '1',
        'environment': 'FTI-CI-AMS',
        'run_mode': 'simple',
        'name': 'This is run name',
        'params': [
            'debugger=vscode',
            'parameter=value'
        ],
        'tests': [
            {
                'test_id': 'TBB-12345'
            },
            {
                'test_id': 'call_op_to_op_just_check_accounts',
                'resources': [
                    {
                        'type': 'ready_accounts',
                        'data': {
                            'accounts': TEST_ACCOUNTS
                        }
                    }
                ]
            }
        ]
    }

    r = client.post('runs', json=request_body)
    assert r.status_code == 201

    # check free slots and running tests
    r = client.get('runstatus')
    expected_response_data = {
        'status': 'running',
        'free_test_slots': 8
    }

    assert r.status_code == 200
    assert r.json() == expected_response_data

    r = client.get('runs/1/running')
    expected_response_data = [
        {
            'test_id': 'TBB-12345'
        },
        {
            'test_id': 'call_op_to_op_just_check_accounts'
        }
    ]

    assert r.status_code == 200
    assert r.json() == expected_response_data

    # patch run (add more tests)
    request_body = {
        'tests': [
            {
                'test_id': 'TBB-12346',
                'rerun_id': 'test_id_2'
            }
        ]
    }

    r = client.patch('runs/1', json=request_body)
    assert r.status_code == 200

    # check free slots and running tests
    r = client.get('runstatus')
    expected_response_data = {
        'status': 'running',
        'free_test_slots': 7
    }

    assert r.status_code == 200
    assert r.json() == expected_response_data

    r = client.get('runs/1/running')
    expected_response_data = [
        {
            'test_id': 'TBB-12345'
        },
        {
            'test_id': 'call_op_to_op_just_check_accounts'
        },
        {
            'test_id': 'TBB-12346'
        }
    ]

    assert r.status_code == 200
    assert r.json() == expected_response_data

    # wait until tests finished
    while True:
        r = client.get('runstatus')
        if r.json()['status'] == 'pending':
            break
        sleep(5)

    sleep(60)  # wait until last publish timeout shoots

    # check reports pagination
    r = client.get('runs/1')
    response_data = r.json()

    assert r.status_code == 200
    assert response_data['run_id'] == '1'
    assert response_data['status'] == 'pending'
    assert response_data['passed'] == {'count': 1, 'last_page': 0}
    assert response_data['failed'] == {'count': 0, 'last_page': -1}
    assert response_data['skipped'] == {'count': 2, 'last_page': 0}
    assert response_data['running'] == {'count': 0}

    r = client.get('runs/1/passed/0')
    response_data = r.json()

    expected_response_data = [
        {
            'test_id': 'call_op_to_op_just_check_accounts',
            'resources': {
                'type': 'ready_accounts',
                'data': {
                    'accounts': [
                        'AGS.TAF.ICDR_1'
                    ]
                }
            }
        }
    ]

    assert r.status_code == 200
    for test in response_data:
        assert test in expected_response_data

    r = client.get('runs/1/skipped/0')
    response_data = r.json()

    expected_response_data = [
        {
            'test_id': 'TBB-12345'
        },
        {
            'test_id': 'TBB-12346'
        }
    ]

    assert r.status_code == 200
    for test in response_data:
        assert test in expected_response_data

    # check free slots
    r = client.get('runstatus')
    expected_response_data = {
        'status': 'pending',
        'free_test_slots': 10
    }

    assert r.status_code == 200
    assert r.json() == expected_response_data

    # delete run
    r = client.delete('runs/1')
    assert r.status_code == 200

    # check runs and free slots
    r = client.get('runs')
    assert r.status_code == 200
    assert r.json() == []

    r = client.get('runstatus')
    expected_response_data = {
        'status': 'pending',
        'free_test_slots': 10
    }

    assert r.status_code == 200
    assert r.json() == expected_response_data

    # terminate pjac instance
    r = client.patch('terminate')
    assert r.status_code == 200


@pytest.mark.integration_test
@pytest.mark.parametrize('pjac_args', [PjacArgs(
    environment='DEV-AUT-AMS',
    help=False,
    mode='account_collector',
    param={},
    release_clean=False,
    repeat=1,
    run=1,
    setting='',
    subset='',
    testcases='',
    trace_enable=False,
    work_threads=10,
    workspace=Paths.workspace()
)])
def test_pjac_in_account_collector_mode(pjac_process, pjac_args):
    """Test PJAC in account_collector mode"""
    url = _wait_pjac_web_service_started(pjac_process['lines_queue'])
    assert url, 'Web service URL not found in process output'

    client = HttpClient(url=url)

    # collect accounts
    request_body = {
        'testcases': [
            'TBB-12345',
            'TBB-12346',
            'call_op_to_op_just_check_accounts'
        ],
        'params': [
            'voice_api_type=pwr'
        ]
    }

    r = client.post('testinfo', json=request_body)
    expected_response_data = {
        'complete': True,
        'accountmap': {
            'TBB-12345': {
                'complete': True,
                'bound': False,
                'accounts': [
                    'TBB.3322L_SP_CID',
                    'AGS.PSTN_HOLDER'
                ]
            },
            'TBB-12346': {
                'complete': True,
                'bound': False,
                'accounts': [
                    'TBB.3322L_SP_CID',
                    'AGS.PSTN_HOLDER'
                ]
            },
            'call_op_to_op_just_check_accounts': {
                'complete': True,
                'bound': False,
                'accounts': [
                    'AGS.TAF.ICDR_1',
                    'AGS.TAF.ICDR_1'
                ]
            }
        }
    }

    assert r.status_code == 200
    assert r.json() == expected_response_data

    # collect accounts with overflow threshold
    request_body = {
        'testcases': [
            'TBB-12345',
            'TBB-12346',
            'TBB-12346',
            'TBB-12346',
            'TBB-12345',
            'TBB-12346',
            'TBB-12346',
            'TBB-12346',
            'TBB-12345',
            'TBB-12346',
            'TBB-12345',
            'TBB-12346',
            'TBB-12346',
            'TBB-12346',
            'TBB-12345',
            'TBB-12346',
            'TBB-12346',
            'TBB-12346',
            'TBB-12345',
            'TBB-12346',
            'TBB-12345',
            'TBB-12346',
            'TBB-12346',
            'TBB-12346',
            'TBB-12345',
            'TBB-12346',
            'TBB-12346',
            'TBB-12346',
            'TBB-12345',
            'TBB-12346',
            'TBB-12346',
            'TBB-12346',
            'call_op_to_op',
            'call_op_to_op'
        ],
        'params': [
            'voice_api_type=pwr'
        ]
    }

    r = client.post('testinfo', json=request_body)
    retry_after = int(r.headers['Retry-After'])

    assert r.status_code == 202
    assert retry_after == 5

    # retry after 5 seconds
    sleep(retry_after)
    r = client.post('testinfo', json=request_body)

    expected_response_data = {
        'complete': True,
        'accountmap': {
            'TBB-12345': {
                'complete': True,
                'bound': False,
                'accounts': [
                    'TBB.3322L_SP_CID',
                    'AGS.PSTN_HOLDER'
                ]
            },
            'TBB-12346': {
                'complete': True,
                'bound': False,
                'accounts': [
                    'TBB.3322L_SP_CID',
                    'AGS.PSTN_HOLDER'
                ]
            },
            'call_op_to_op': {
                'complete': True,
                'bound': False,
                'accounts': [
                    'AGS.TAF.ICDR_1',
                    'AGS.TAF.ICDR_1'
                ]
            }
        }
    }

    assert r.status_code == 200
    assert r.json() == expected_response_data

    # terminate pjac instance
    r = client.patch('terminate')
    assert r.status_code == 200
