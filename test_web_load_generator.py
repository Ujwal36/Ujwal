"""This module contains unit tests for web load generator."""
import os
import time
from functools import partial
from threading import Thread
from unittest.mock import Mock, patch

import pytest
import requests
from wheezy.routing import url

from bl.executor.load_generators.views.web import DowserHandler, TerminationHandler, TraceHandler
from bl.executor.load_generators.web_load_generator import Settings, WebLoadGenerator
from test_framework.common.helpers import next_free_port
from test_framework.common.timer import Stopwatch
from test_framework.common.web_server.base import APIBaseHandler
from test_framework.common.web_server.helpers.views import create_response


@pytest.fixture(scope='module')
def web_load_generator():
    """Web load generator fixture to handle web server start/stop."""
    Settings.address_for_resolving_local_ip = 'google.com'
    main_loop = Mock()
    port = next_free_port('0.0.0.0', 8000, protocol='tcp')
    web_load_generator = WebLoadGenerator(main_loop=main_loop, port=port, threads_count=10)
    yield web_load_generator
    web_load_generator.stop()


def test_web_load_generator_trace(web_load_generator, request_mock):
    """Tests handling of trace request in web load generator."""
    trace_request_mock = request_mock(method='GET', body={})
    trace_response = TraceHandler(trace_request_mock)
    stacktraces = trace_response.buffer[0].decode()
    assert 'STACKTRACE - START' in stacktraces
    assert os.path.abspath(__file__) in stacktraces


@patch('bl.executor.load_generators.views.web.Settings')
@patch('bl.executor.load_generators.views.web.launch_memory_usage_server')
def test_web_load_generator_dowser(memory_server_launch_mock, settings_mock, web_load_generator, request_mock):
    """Tests handling of dowser request in web load generator."""
    dowser_request_mock = request_mock(method='GET', body={})
    dowser_request_mock.host = 'host:0'
    dowser_response = DowserHandler(dowser_request_mock)
    assert dowser_response.status_code == 302
    memory_server_launch_mock.assert_called()
    assert ('Location', 'http://host:1?floor=10') in dowser_response.headers


def test_web_load_generator_termination(web_load_generator, request_mock):
    """Tests handling of termination request in web load generator."""
    termination_request_mock = request_mock(method='PATCH', body={})
    main_loop = web_load_generator.main_loop
    route_args = {'route_args': {'main_loop': main_loop}}
    termination_request_mock.environ.update(route_args)
    termination_response = TerminationHandler(termination_request_mock)
    assert termination_response.status_code == 200
    main_loop.stop.assert_called()


def test_web_load_simultaneous(web_load_generator):
    response_time = 2
    simultaneous_threads = web_load_generator.thread_count

    # Create and add dummy handler

    class SleepAndResponse(APIBaseHandler):
        def get(self):
            time.sleep(response_time)
            return create_response(status_code=200, data='')

    web_load_generator.path_router.add_routes([url('unittest', SleepAndResponse)])
    address = web_load_generator.address

    def collect_response(to):
        to.append(requests.get(f'{address}/unittest').status_code)

    results = []
    threads = [Thread(target=partial(collect_response, results)) for _ in range(simultaneous_threads)]

    # Start simultaneous requests
    for thread in threads:
        thread.start()
    stopwatch = Stopwatch()

    # Wait for results
    for thread in threads:
        thread.join()
    stopwatch.stop()

    assert stopwatch.elapsed == pytest.approx(response_time, 0.1)
    assert results == [200] * simultaneous_threads
