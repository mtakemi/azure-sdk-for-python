# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar, Union

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._operations import build_template_spec_versions_create_or_update_request, build_template_spec_versions_delete_request, build_template_spec_versions_get_request, build_template_spec_versions_list_request, build_template_spec_versions_update_request, build_template_specs_create_or_update_request, build_template_specs_delete_request, build_template_specs_get_request, build_template_specs_list_by_resource_group_request, build_template_specs_list_by_subscription_request, build_template_specs_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TemplateSpecsOperations:
    """TemplateSpecsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.templatespecs.v2021_05_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        template_spec_name: str,
        template_spec: "_models.TemplateSpec",
        **kwargs: Any
    ) -> "_models.TemplateSpec":
        """Creates or updates a Template Spec.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param template_spec: Template Spec supplied to the operation.
        :type template_spec: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpec
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TemplateSpec, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpec
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpec"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(template_spec, 'TemplateSpec')

        request = build_template_specs_create_or_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('TemplateSpec', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('TemplateSpec', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}"}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        template_spec_name: str,
        template_spec: Optional["_models.TemplateSpecUpdateModel"] = None,
        **kwargs: Any
    ) -> "_models.TemplateSpec":
        """Updates Template Spec tags with specified values.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param template_spec: Template Spec resource with the tags to be updated. Default value is
         None.
        :type template_spec:
         ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecUpdateModel
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TemplateSpec, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpec
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpec"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if template_spec is not None:
            _json = self._serialize.body(template_spec, 'TemplateSpecUpdateModel')
        else:
            _json = None

        request = build_template_specs_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TemplateSpec', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}"}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        template_spec_name: str,
        expand: Optional[Union[str, "_models.TemplateSpecExpandKind"]] = None,
        **kwargs: Any
    ) -> "_models.TemplateSpec":
        """Gets a Template Spec with a given name.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param expand: Allows for expansion of additional Template Spec details in the response.
         Optional. Default value is None.
        :type expand: str or
         ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecExpandKind
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TemplateSpec, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpec
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpec"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str

        
        request = build_template_specs_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            api_version=api_version,
            expand=expand,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TemplateSpec', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}"}  # type: ignore


    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        template_spec_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a Template Spec by name. When operation completes, status code 200 returned without
        content.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str

        
        request = build_template_specs_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}"}  # type: ignore


    @distributed_trace
    def list_by_subscription(
        self,
        expand: Optional[Union[str, "_models.TemplateSpecExpandKind"]] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.TemplateSpecsListResult"]:
        """Lists all the Template Specs within the specified subscriptions.

        :param expand: Allows for expansion of additional Template Spec details in the response.
         Optional. Default value is None.
        :type expand: str or
         ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecExpandKind
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TemplateSpecsListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpecsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_template_specs_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    expand=expand,
                    template_url=self.list_by_subscription.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_template_specs_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("TemplateSpecsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Resources/templateSpecs/"}  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self,
        resource_group_name: str,
        expand: Optional[Union[str, "_models.TemplateSpecExpandKind"]] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.TemplateSpecsListResult"]:
        """Lists all the Template Specs within the specified resource group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param expand: Allows for expansion of additional Template Spec details in the response.
         Optional. Default value is None.
        :type expand: str or
         ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecExpandKind
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TemplateSpecsListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpecsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_template_specs_list_by_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    api_version=api_version,
                    expand=expand,
                    template_url=self.list_by_resource_group.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_template_specs_list_by_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("TemplateSpecsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/"}  # type: ignore
class TemplateSpecVersionsOperations:
    """TemplateSpecVersionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.templatespecs.v2021_05_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        template_spec_name: str,
        template_spec_version: str,
        template_spec_version_model: "_models.TemplateSpecVersion",
        **kwargs: Any
    ) -> "_models.TemplateSpecVersion":
        """Creates or updates a Template Spec version.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param template_spec_version: The version of the Template Spec.
        :type template_spec_version: str
        :param template_spec_version_model: Template Spec Version supplied to the operation.
        :type template_spec_version_model:
         ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersion
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TemplateSpecVersion, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersion
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpecVersion"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(template_spec_version_model, 'TemplateSpecVersion')

        request = build_template_spec_versions_create_or_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            template_spec_version=template_spec_version,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('TemplateSpecVersion', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('TemplateSpecVersion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}"}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        template_spec_name: str,
        template_spec_version: str,
        template_spec_version_update_model: Optional["_models.TemplateSpecVersionUpdateModel"] = None,
        **kwargs: Any
    ) -> "_models.TemplateSpecVersion":
        """Updates Template Spec Version tags with specified values.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param template_spec_version: The version of the Template Spec.
        :type template_spec_version: str
        :param template_spec_version_update_model: Template Spec Version resource with the tags to be
         updated. Default value is None.
        :type template_spec_version_update_model:
         ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersionUpdateModel
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TemplateSpecVersion, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersion
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpecVersion"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if template_spec_version_update_model is not None:
            _json = self._serialize.body(template_spec_version_update_model, 'TemplateSpecVersionUpdateModel')
        else:
            _json = None

        request = build_template_spec_versions_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            template_spec_version=template_spec_version,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TemplateSpecVersion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}"}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        template_spec_name: str,
        template_spec_version: str,
        **kwargs: Any
    ) -> "_models.TemplateSpecVersion":
        """Gets a Template Spec version from a specific Template Spec.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param template_spec_version: The version of the Template Spec.
        :type template_spec_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TemplateSpecVersion, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersion
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpecVersion"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str

        
        request = build_template_spec_versions_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            template_spec_version=template_spec_version,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TemplateSpecVersion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}"}  # type: ignore


    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        template_spec_name: str,
        template_spec_version: str,
        **kwargs: Any
    ) -> None:
        """Deletes a specific version from a Template Spec. When operation completes, status code 200
        returned without content.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param template_spec_version: The version of the Template Spec.
        :type template_spec_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str

        
        request = build_template_spec_versions_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            template_spec_version=template_spec_version,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}"}  # type: ignore


    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        template_spec_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.TemplateSpecVersionsListResult"]:
        """Lists all the Template Spec versions in the specified Template Spec.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TemplateSpecVersionsListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersionsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpecVersionsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_template_spec_versions_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    template_spec_name=template_spec_name,
                    api_version=api_version,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_template_spec_versions_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    template_spec_name=template_spec_name,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("TemplateSpecVersionsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions"}  # type: ignore
