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
from spotify_python_sdk.model.playlists_add_items_request import PlaylistsAddItemsRequest as PlaylistsAddItemsRequestSchema
from spotify_python_sdk.model.playlists_remove_items_response import PlaylistsRemoveItemsResponse as PlaylistsRemoveItemsResponseSchema
from spotify_python_sdk.model.albums_get_information_response import AlbumsGetInformationResponse as AlbumsGetInformationResponseSchema
from spotify_python_sdk.model.playlists_add_items_request_uris import PlaylistsAddItemsRequestUris as PlaylistsAddItemsRequestUrisSchema
from spotify_python_sdk.model.albums_get_information429_response import AlbumsGetInformation429Response as AlbumsGetInformation429ResponseSchema

from spotify_python_sdk.type.albums_get_information_response import AlbumsGetInformationResponse
from spotify_python_sdk.type.albums_get_information429_response import AlbumsGetInformation429Response
from spotify_python_sdk.type.playlists_add_items_request import PlaylistsAddItemsRequest
from spotify_python_sdk.type.playlists_remove_items_response import PlaylistsRemoveItemsResponse
from spotify_python_sdk.type.playlists_add_items_request_uris import PlaylistsAddItemsRequestUris
from spotify_python_sdk.type.albums_get_information403_response import AlbumsGetInformation403Response

from ...api_client import Dictionary
from spotify_python_sdk.pydantic.playlists_add_items_request_uris import PlaylistsAddItemsRequestUris as PlaylistsAddItemsRequestUrisPydantic
from spotify_python_sdk.pydantic.playlists_remove_items_response import PlaylistsRemoveItemsResponse as PlaylistsRemoveItemsResponsePydantic
from spotify_python_sdk.pydantic.albums_get_information_response import AlbumsGetInformationResponse as AlbumsGetInformationResponsePydantic
from spotify_python_sdk.pydantic.playlists_add_items_request import PlaylistsAddItemsRequest as PlaylistsAddItemsRequestPydantic
from spotify_python_sdk.pydantic.albums_get_information403_response import AlbumsGetInformation403Response as AlbumsGetInformation403ResponsePydantic
from spotify_python_sdk.pydantic.albums_get_information429_response import AlbumsGetInformation429Response as AlbumsGetInformation429ResponsePydantic

# Query params
PositionSchema = schemas.IntSchema
UrisSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'position': typing.Union[PositionSchema, decimal.Decimal, int, ],
        'uris': typing.Union[UrisSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_position = api_client.QueryParameter(
    name="position",
    style=api_client.ParameterStyle.FORM,
    schema=PositionSchema,
    explode=True,
)
request_query_uris = api_client.QueryParameter(
    name="uris",
    style=api_client.ParameterStyle.FORM,
    schema=UrisSchema,
    explode=True,
)
# Path params
PlaylistIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'playlist_id': typing.Union[PlaylistIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_playlist_id = api_client.PathParameter(
    name="playlist_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PlaylistIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = PlaylistsAddItemsRequestSchema


request_body_playlists_add_items_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = PlaylistsRemoveItemsResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: PlaylistsRemoveItemsResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: PlaylistsRemoveItemsResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_items_mapped_args(
        self,
        playlist_id: str,
        uris: typing.Optional[PlaylistsAddItemsRequestUris] = None,
        position: typing.Optional[int] = None,
        position: typing.Optional[int] = None,
        uris: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if uris is not None:
            _body["uris"] = uris
        if position is not None:
            _body["position"] = position
        args.body = _body
        if position is not None:
            _query_params["position"] = position
        if uris is not None:
            _query_params["uris"] = uris
        if playlist_id is not None:
            _path_params["playlist_id"] = playlist_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aadd_items_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Add Items to Playlist 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_playlist_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_position,
            request_query_uris,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/playlists/{playlist_id}/tracks',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_playlists_add_items_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _add_items_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add Items to Playlist 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_playlist_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_position,
            request_query_uris,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/playlists/{playlist_id}/tracks',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_playlists_add_items_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class AddItemsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_items(
        self,
        playlist_id: str,
        uris: typing.Optional[PlaylistsAddItemsRequestUris] = None,
        position: typing.Optional[int] = None,
        position: typing.Optional[int] = None,
        uris: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_items_mapped_args(
            playlist_id=playlist_id,
            uris=uris,
            position=position,
            position=position,
            uris=uris,
        )
        return await self._aadd_items_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def add_items(
        self,
        playlist_id: str,
        uris: typing.Optional[PlaylistsAddItemsRequestUris] = None,
        position: typing.Optional[int] = None,
        position: typing.Optional[int] = None,
        uris: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_items_mapped_args(
            playlist_id=playlist_id,
            uris=uris,
            position=position,
            position=position,
            uris=uris,
        )
        return self._add_items_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class AddItems(BaseApi):

    async def aadd_items(
        self,
        playlist_id: str,
        uris: typing.Optional[PlaylistsAddItemsRequestUris] = None,
        position: typing.Optional[int] = None,
        position: typing.Optional[int] = None,
        uris: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PlaylistsRemoveItemsResponsePydantic:
        raw_response = await self.raw.aadd_items(
            playlist_id=playlist_id,
            uris=uris,
            position=position,
            position=position,
            uris=uris,
            **kwargs,
        )
        if validate:
            return PlaylistsRemoveItemsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PlaylistsRemoveItemsResponsePydantic, raw_response.body)
    
    
    def add_items(
        self,
        playlist_id: str,
        uris: typing.Optional[PlaylistsAddItemsRequestUris] = None,
        position: typing.Optional[int] = None,
        position: typing.Optional[int] = None,
        uris: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PlaylistsRemoveItemsResponsePydantic:
        raw_response = self.raw.add_items(
            playlist_id=playlist_id,
            uris=uris,
            position=position,
            position=position,
            uris=uris,
        )
        if validate:
            return PlaylistsRemoveItemsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PlaylistsRemoveItemsResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        playlist_id: str,
        uris: typing.Optional[PlaylistsAddItemsRequestUris] = None,
        position: typing.Optional[int] = None,
        position: typing.Optional[int] = None,
        uris: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_items_mapped_args(
            playlist_id=playlist_id,
            uris=uris,
            position=position,
            position=position,
            uris=uris,
        )
        return await self._aadd_items_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        playlist_id: str,
        uris: typing.Optional[PlaylistsAddItemsRequestUris] = None,
        position: typing.Optional[int] = None,
        position: typing.Optional[int] = None,
        uris: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_items_mapped_args(
            playlist_id=playlist_id,
            uris=uris,
            position=position,
            position=position,
            uris=uris,
        )
        return self._add_items_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

