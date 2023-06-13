"""This module contains unit tests for service load generator."""
from unittest.mock import Mock

import pytest

from bl.executor.load_generators.response_validator import ResponseValidator
from bl.executor.load_generators.service_load_generator import ApiVersionHandler, ServiceLoadGenerator
from test_framework.common.binaries.version import Version
from test_framework.paths import Paths


@pytest.fixture(scope='module')
def service_load_generator():
    """Service load generator fixture."""
    stress_generator = ServiceLoadGenerator(test_factory=Mock(), workers=Mock(), load_generator=Mock())
    yield stress_generator
    stress_generator.stop()


def test_service_load_generator_apiversion_route(service_load_generator, request_mock):
    """Tests '/apiversion' route in service load generator."""
    routes = service_load_generator.create_routes()
    route = next(r for r in routes if r[0] == 'apiversion')
    route_handler, route_args = route[1], route[2]
    request = request_mock(method='GET', body={})
    if route_args:
        request.environ.update({'route_args': route_args})
    response = route_handler(request)
    assert response.status_code == 200


def test_service_load_generator_serviceversion_route(service_load_generator, request_mock):
    """Tests '/serviceversion' route in service load generator."""
    routes = service_load_generator.create_routes()
    route = next(r for r in routes if r[0] == 'serviceversion')
    route_handler, route_args = route[1], route[2]
    request = request_mock(method='GET', body={})
    if route_args:
        request.environ.update({'route_args': route_args})
    response = route_handler(request)
    assert response.status_code == 200


def test_service_load_generator_apiversion(request_mock):
    """Tests handling of '/apiversion' request in service load generator."""
    api_version_request = request_mock(method='GET', body={})
    route_args = {'route_args': {'service_response_validator': ResponseValidator(Paths.pjac_instance_api())}}
    api_version_request.environ.update(route_args)
    api_version_response = ApiVersionHandler(api_version_request)
    assert api_version_response.status_code == 200
    assert api_version_response.buffer[0].decode() == Version.api(Paths.pjac_instance_api())
