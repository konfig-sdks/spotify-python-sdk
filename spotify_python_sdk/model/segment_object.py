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


class SegmentObject(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            start = schemas.NumberSchema
            duration = schemas.NumberSchema
            
            
            class confidence(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 1
                    inclusive_minimum = 0
            loudness_start = schemas.NumberSchema
            loudness_max = schemas.NumberSchema
            loudness_max_time = schemas.NumberSchema
            loudness_end = schemas.NumberSchema
        
            @staticmethod
            def pitches() -> typing.Type['SegmentObjectPitches']:
                return SegmentObjectPitches
        
            @staticmethod
            def timbre() -> typing.Type['SegmentObjectTimbre']:
                return SegmentObjectTimbre
            __annotations__ = {
                "start": start,
                "duration": duration,
                "confidence": confidence,
                "loudness_start": loudness_start,
                "loudness_max": loudness_max,
                "loudness_max_time": loudness_max_time,
                "loudness_end": loudness_end,
                "pitches": pitches,
                "timbre": timbre,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confidence"]) -> MetaOapg.properties.confidence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loudness_start"]) -> MetaOapg.properties.loudness_start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loudness_max"]) -> MetaOapg.properties.loudness_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loudness_max_time"]) -> MetaOapg.properties.loudness_max_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loudness_end"]) -> MetaOapg.properties.loudness_end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pitches"]) -> 'SegmentObjectPitches': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timbre"]) -> 'SegmentObjectTimbre': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["start", "duration", "confidence", "loudness_start", "loudness_max", "loudness_max_time", "loudness_end", "pitches", "timbre", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> typing.Union[MetaOapg.properties.start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confidence"]) -> typing.Union[MetaOapg.properties.confidence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loudness_start"]) -> typing.Union[MetaOapg.properties.loudness_start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loudness_max"]) -> typing.Union[MetaOapg.properties.loudness_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loudness_max_time"]) -> typing.Union[MetaOapg.properties.loudness_max_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loudness_end"]) -> typing.Union[MetaOapg.properties.loudness_end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pitches"]) -> typing.Union['SegmentObjectPitches', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timbre"]) -> typing.Union['SegmentObjectTimbre', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["start", "duration", "confidence", "loudness_start", "loudness_max", "loudness_max_time", "loudness_end", "pitches", "timbre", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        start: typing.Union[MetaOapg.properties.start, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        confidence: typing.Union[MetaOapg.properties.confidence, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        loudness_start: typing.Union[MetaOapg.properties.loudness_start, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        loudness_max: typing.Union[MetaOapg.properties.loudness_max, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        loudness_max_time: typing.Union[MetaOapg.properties.loudness_max_time, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        loudness_end: typing.Union[MetaOapg.properties.loudness_end, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pitches: typing.Union['SegmentObjectPitches', schemas.Unset] = schemas.unset,
        timbre: typing.Union['SegmentObjectTimbre', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SegmentObject':
        return super().__new__(
            cls,
            *args,
            start=start,
            duration=duration,
            confidence=confidence,
            loudness_start=loudness_start,
            loudness_max=loudness_max,
            loudness_max_time=loudness_max_time,
            loudness_end=loudness_end,
            pitches=pitches,
            timbre=timbre,
            _configuration=_configuration,
            **kwargs,
        )

from spotify_python_sdk.model.segment_object_pitches import SegmentObjectPitches
from spotify_python_sdk.model.segment_object_timbre import SegmentObjectTimbre
