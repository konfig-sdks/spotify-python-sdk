# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from spotify_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from spotify_python_sdk.api_response import AsyncGeneratorResponse
from spotify_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from spotify_python_sdk import schemas  # noqa: F401

from spotify_python_sdk.model.albums_get_information403_response import AlbumsGetInformation403Response as AlbumsGetInformation403ResponseSchema
from spotify_python_sdk.model.albums_list_several_response import AlbumsListSeveralResponse as AlbumsListSeveralResponseSchema
from spotify_python_sdk.model.albums_get_information_response import AlbumsGetInformationResponse as AlbumsGetInformationResponseSchema
from spotify_python_sdk.model.albums_get_information429_response import AlbumsGetInformation429Response as AlbumsGetInformation429ResponseSchema

from spotify_python_sdk.type.albums_get_information_response import AlbumsGetInformationResponse
from spotify_python_sdk.type.albums_get_information429_response import AlbumsGetInformation429Response
from spotify_python_sdk.type.albums_list_several_response import AlbumsListSeveralResponse
from spotify_python_sdk.type.albums_get_information403_response import AlbumsGetInformation403Response

from ...api_client import Dictionary
from spotify_python_sdk.pydantic.albums_get_information_response import AlbumsGetInformationResponse as AlbumsGetInformationResponsePydantic
from spotify_python_sdk.pydantic.albums_get_information403_response import AlbumsGetInformation403Response as AlbumsGetInformation403ResponsePydantic
from spotify_python_sdk.pydantic.albums_list_several_response import AlbumsListSeveralResponse as AlbumsListSeveralResponsePydantic
from spotify_python_sdk.pydantic.albums_get_information429_response import AlbumsGetInformation429Response as AlbumsGetInformation429ResponsePydantic

from . import path

# Query params
IdsSchema = schemas.StrSchema
MarketSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'ids': typing.Union[IdsSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'market': typing.Union[MarketSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_ids = api_client.QueryParameter(
    name="ids",
    style=api_client.ParameterStyle.FORM,
    schema=IdsSchema,
    required=True,
    explode=True,
)
request_query_market = api_client.QueryParameter(
    name="market",
    style=api_client.ParameterStyle.FORM,
    schema=MarketSchema,
    explode=True,
)
_auth = [
    'oauth_2_0',
]
SchemaFor200ResponseBodyApplicationJson = AlbumsListSeveralResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AlbumsListSeveralResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AlbumsListSeveralResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = AlbumsGetInformationResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: AlbumsGetInformationResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: AlbumsGetInformationResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = AlbumsGetInformation403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: AlbumsGetInformation403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: AlbumsGetInformation403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor429ResponseBodyApplicationJson = AlbumsGetInformation429ResponseSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: AlbumsGetInformation429Response


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: AlbumsGetInformation429Response


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    '403': _response_for_403,
    '429': _response_for_429,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_several_mapped_args(
        self,
        ids: str,
        market: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if ids is not None:
            _query_params["ids"] = ids
        if market is not None:
            _query_params["market"] = market
        args.query = _query_params
        return args

    async def _alist_several_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Several Albums 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_ids,
            request_query_market,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/albums',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_several_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Several Albums 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_ids,
            request_query_market,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/albums',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListSeveralRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_several(
        self,
        ids: str,
        market: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_several_mapped_args(
            ids=ids,
            market=market,
        )
        return await self._alist_several_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_several(
        self,
        ids: str,
        market: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_several_mapped_args(
            ids=ids,
            market=market,
        )
        return self._list_several_oapg(
            query_params=args.query,
        )

class ListSeveral(BaseApi):

    async def alist_several(
        self,
        ids: str,
        market: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AlbumsListSeveralResponsePydantic:
        raw_response = await self.raw.alist_several(
            ids=ids,
            market=market,
            **kwargs,
        )
        if validate:
            return AlbumsListSeveralResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AlbumsListSeveralResponsePydantic, raw_response.body)
    
    
    def list_several(
        self,
        ids: str,
        market: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AlbumsListSeveralResponsePydantic:
        raw_response = self.raw.list_several(
            ids=ids,
            market=market,
        )
        if validate:
            return AlbumsListSeveralResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AlbumsListSeveralResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        ids: str,
        market: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_several_mapped_args(
            ids=ids,
            market=market,
        )
        return await self._alist_several_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        ids: str,
        market: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_several_mapped_args(
            ids=ids,
            market=market,
        )
        return self._list_several_oapg(
            query_params=args.query,
        )

