# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(resource_uri: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{resourceUri}/providers/microsoft.insights/diagnosticSettings/service")
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(resource_uri: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{resourceUri}/providers/microsoft.insights/diagnosticSettings/service")
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_request(resource_uri: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{resourceUri}/providers/microsoft.insights/diagnosticSettings/service")
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


class ServiceDiagnosticSettingsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~$(python-base-namespace).v2016_09_01.MonitorManagementClient`'s
        :attr:`service_diagnostic_settings` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(self, resource_uri: str, **kwargs: Any) -> _models.ServiceDiagnosticSettingsResource:
        """Gets the active diagnostic settings for the specified resource. **WARNING**\ : This method will
        be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ServiceDiagnosticSettingsResource]

        request = build_get_request(
            resource_uri=resource_uri,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ServiceDiagnosticSettingsResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{resourceUri}/providers/microsoft.insights/diagnosticSettings/service"}  # type: ignore

    @overload
    def create_or_update(
        self,
        resource_uri: str,
        parameters: _models.ServiceDiagnosticSettingsResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Create or update new diagnostic settings for the specified resource. **WARNING**\ : This method
        will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param parameters: Parameters supplied to the operation. Required.
        :type parameters:
         ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self, resource_uri: str, parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Create or update new diagnostic settings for the specified resource. **WARNING**\ : This method
        will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param parameters: Parameters supplied to the operation. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self, resource_uri: str, parameters: Union[_models.ServiceDiagnosticSettingsResource, IO], **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Create or update new diagnostic settings for the specified resource. **WARNING**\ : This method
        will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param parameters: Parameters supplied to the operation. Is either a model type or a IO type.
         Required.
        :type parameters:
         ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResource or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ServiceDiagnosticSettingsResource]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ServiceDiagnosticSettingsResource")

        request = build_create_or_update_request(
            resource_uri=resource_uri,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ServiceDiagnosticSettingsResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/{resourceUri}/providers/microsoft.insights/diagnosticSettings/service"}  # type: ignore

    @overload
    def update(
        self,
        resource_uri: str,
        service_diagnostic_settings_resource: _models.ServiceDiagnosticSettingsResourcePatch,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Updates an existing ServiceDiagnosticSettingsResource. To update other fields use the
        CreateOrUpdate method. **WARNING**\ : This method will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param service_diagnostic_settings_resource: Parameters supplied to the operation. Required.
        :type service_diagnostic_settings_resource:
         ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResourcePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        resource_uri: str,
        service_diagnostic_settings_resource: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Updates an existing ServiceDiagnosticSettingsResource. To update other fields use the
        CreateOrUpdate method. **WARNING**\ : This method will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param service_diagnostic_settings_resource: Parameters supplied to the operation. Required.
        :type service_diagnostic_settings_resource: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(
        self,
        resource_uri: str,
        service_diagnostic_settings_resource: Union[_models.ServiceDiagnosticSettingsResourcePatch, IO],
        **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Updates an existing ServiceDiagnosticSettingsResource. To update other fields use the
        CreateOrUpdate method. **WARNING**\ : This method will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param service_diagnostic_settings_resource: Parameters supplied to the operation. Is either a
         model type or a IO type. Required.
        :type service_diagnostic_settings_resource:
         ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResourcePatch or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2016_09_01.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ServiceDiagnosticSettingsResource]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(service_diagnostic_settings_resource, (IO, bytes)):
            _content = service_diagnostic_settings_resource
        else:
            _json = self._serialize.body(service_diagnostic_settings_resource, "ServiceDiagnosticSettingsResourcePatch")

        request = build_update_request(
            resource_uri=resource_uri,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ServiceDiagnosticSettingsResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/{resourceUri}/providers/microsoft.insights/diagnosticSettings/service"}  # type: ignore
