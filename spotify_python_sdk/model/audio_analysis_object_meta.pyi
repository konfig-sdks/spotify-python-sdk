# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

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


class AudioAnalysisObjectMeta(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            analyzer_version = schemas.StrSchema
            platform = schemas.StrSchema
            detailed_status = schemas.StrSchema
            status_code = schemas.IntSchema
            timestamp = schemas.IntSchema
            analysis_time = schemas.NumberSchema
            input_process = schemas.StrSchema
            __annotations__ = {
                "analyzer_version": analyzer_version,
                "platform": platform,
                "detailed_status": detailed_status,
                "status_code": status_code,
                "timestamp": timestamp,
                "analysis_time": analysis_time,
                "input_process": input_process,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analyzer_version"]) -> MetaOapg.properties.analyzer_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform"]) -> MetaOapg.properties.platform: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detailed_status"]) -> MetaOapg.properties.detailed_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_code"]) -> MetaOapg.properties.status_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analysis_time"]) -> MetaOapg.properties.analysis_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_process"]) -> MetaOapg.properties.input_process: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["analyzer_version", "platform", "detailed_status", "status_code", "timestamp", "analysis_time", "input_process", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analyzer_version"]) -> typing.Union[MetaOapg.properties.analyzer_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform"]) -> typing.Union[MetaOapg.properties.platform, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detailed_status"]) -> typing.Union[MetaOapg.properties.detailed_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_code"]) -> typing.Union[MetaOapg.properties.status_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analysis_time"]) -> typing.Union[MetaOapg.properties.analysis_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_process"]) -> typing.Union[MetaOapg.properties.input_process, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["analyzer_version", "platform", "detailed_status", "status_code", "timestamp", "analysis_time", "input_process", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        analyzer_version: typing.Union[MetaOapg.properties.analyzer_version, str, schemas.Unset] = schemas.unset,
        platform: typing.Union[MetaOapg.properties.platform, str, schemas.Unset] = schemas.unset,
        detailed_status: typing.Union[MetaOapg.properties.detailed_status, str, schemas.Unset] = schemas.unset,
        status_code: typing.Union[MetaOapg.properties.status_code, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        timestamp: typing.Union[MetaOapg.properties.timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        analysis_time: typing.Union[MetaOapg.properties.analysis_time, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        input_process: typing.Union[MetaOapg.properties.input_process, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AudioAnalysisObjectMeta':
        return super().__new__(
            cls,
            *args,
            analyzer_version=analyzer_version,
            platform=platform,
            detailed_status=detailed_status,
            status_code=status_code,
            timestamp=timestamp,
            analysis_time=analysis_time,
            input_process=input_process,
            _configuration=_configuration,
            **kwargs,
        )
