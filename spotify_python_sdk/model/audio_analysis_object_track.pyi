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


class AudioAnalysisObjectTrack(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            num_samples = schemas.IntSchema
            duration = schemas.NumberSchema
            sample_md5 = schemas.StrSchema
            offset_seconds = schemas.IntSchema
            window_seconds = schemas.IntSchema
            analysis_sample_rate = schemas.IntSchema
            analysis_channels = schemas.IntSchema
            end_of_fade_in = schemas.NumberSchema
            start_of_fade_out = schemas.NumberSchema
            loudness = schemas.Float32Schema
            tempo = schemas.Float32Schema
            
            
            class tempo_confidence(
                schemas.NumberSchema
            ):
                pass
        
            @staticmethod
            def time_signature() -> typing.Type['TimeSignature']:
                return TimeSignature
            
            
            class time_signature_confidence(
                schemas.NumberSchema
            ):
                pass
        
            @staticmethod
            def key() -> typing.Type['Key']:
                return Key
            
            
            class key_confidence(
                schemas.NumberSchema
            ):
                pass
            mode = schemas.IntSchema
            
            
            class mode_confidence(
                schemas.NumberSchema
            ):
                pass
            codestring = schemas.StrSchema
            code_version = schemas.NumberSchema
            echoprintstring = schemas.StrSchema
            echoprint_version = schemas.NumberSchema
            synchstring = schemas.StrSchema
            synch_version = schemas.NumberSchema
            rhythmstring = schemas.StrSchema
            rhythm_version = schemas.NumberSchema
            __annotations__ = {
                "num_samples": num_samples,
                "duration": duration,
                "sample_md5": sample_md5,
                "offset_seconds": offset_seconds,
                "window_seconds": window_seconds,
                "analysis_sample_rate": analysis_sample_rate,
                "analysis_channels": analysis_channels,
                "end_of_fade_in": end_of_fade_in,
                "start_of_fade_out": start_of_fade_out,
                "loudness": loudness,
                "tempo": tempo,
                "tempo_confidence": tempo_confidence,
                "time_signature": time_signature,
                "time_signature_confidence": time_signature_confidence,
                "key": key,
                "key_confidence": key_confidence,
                "mode": mode,
                "mode_confidence": mode_confidence,
                "codestring": codestring,
                "code_version": code_version,
                "echoprintstring": echoprintstring,
                "echoprint_version": echoprint_version,
                "synchstring": synchstring,
                "synch_version": synch_version,
                "rhythmstring": rhythmstring,
                "rhythm_version": rhythm_version,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["num_samples"]) -> MetaOapg.properties.num_samples: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sample_md5"]) -> MetaOapg.properties.sample_md5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["offset_seconds"]) -> MetaOapg.properties.offset_seconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["window_seconds"]) -> MetaOapg.properties.window_seconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analysis_sample_rate"]) -> MetaOapg.properties.analysis_sample_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analysis_channels"]) -> MetaOapg.properties.analysis_channels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_of_fade_in"]) -> MetaOapg.properties.end_of_fade_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_of_fade_out"]) -> MetaOapg.properties.start_of_fade_out: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loudness"]) -> MetaOapg.properties.loudness: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tempo"]) -> MetaOapg.properties.tempo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tempo_confidence"]) -> MetaOapg.properties.tempo_confidence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_signature"]) -> 'TimeSignature': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_signature_confidence"]) -> MetaOapg.properties.time_signature_confidence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> 'Key': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key_confidence"]) -> MetaOapg.properties.key_confidence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode"]) -> MetaOapg.properties.mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode_confidence"]) -> MetaOapg.properties.mode_confidence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["codestring"]) -> MetaOapg.properties.codestring: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code_version"]) -> MetaOapg.properties.code_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["echoprintstring"]) -> MetaOapg.properties.echoprintstring: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["echoprint_version"]) -> MetaOapg.properties.echoprint_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["synchstring"]) -> MetaOapg.properties.synchstring: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["synch_version"]) -> MetaOapg.properties.synch_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rhythmstring"]) -> MetaOapg.properties.rhythmstring: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rhythm_version"]) -> MetaOapg.properties.rhythm_version: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["num_samples", "duration", "sample_md5", "offset_seconds", "window_seconds", "analysis_sample_rate", "analysis_channels", "end_of_fade_in", "start_of_fade_out", "loudness", "tempo", "tempo_confidence", "time_signature", "time_signature_confidence", "key", "key_confidence", "mode", "mode_confidence", "codestring", "code_version", "echoprintstring", "echoprint_version", "synchstring", "synch_version", "rhythmstring", "rhythm_version", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["num_samples"]) -> typing.Union[MetaOapg.properties.num_samples, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sample_md5"]) -> typing.Union[MetaOapg.properties.sample_md5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["offset_seconds"]) -> typing.Union[MetaOapg.properties.offset_seconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["window_seconds"]) -> typing.Union[MetaOapg.properties.window_seconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analysis_sample_rate"]) -> typing.Union[MetaOapg.properties.analysis_sample_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analysis_channels"]) -> typing.Union[MetaOapg.properties.analysis_channels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_of_fade_in"]) -> typing.Union[MetaOapg.properties.end_of_fade_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_of_fade_out"]) -> typing.Union[MetaOapg.properties.start_of_fade_out, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loudness"]) -> typing.Union[MetaOapg.properties.loudness, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tempo"]) -> typing.Union[MetaOapg.properties.tempo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tempo_confidence"]) -> typing.Union[MetaOapg.properties.tempo_confidence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_signature"]) -> typing.Union['TimeSignature', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_signature_confidence"]) -> typing.Union[MetaOapg.properties.time_signature_confidence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union['Key', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key_confidence"]) -> typing.Union[MetaOapg.properties.key_confidence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode"]) -> typing.Union[MetaOapg.properties.mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode_confidence"]) -> typing.Union[MetaOapg.properties.mode_confidence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["codestring"]) -> typing.Union[MetaOapg.properties.codestring, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code_version"]) -> typing.Union[MetaOapg.properties.code_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["echoprintstring"]) -> typing.Union[MetaOapg.properties.echoprintstring, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["echoprint_version"]) -> typing.Union[MetaOapg.properties.echoprint_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["synchstring"]) -> typing.Union[MetaOapg.properties.synchstring, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["synch_version"]) -> typing.Union[MetaOapg.properties.synch_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rhythmstring"]) -> typing.Union[MetaOapg.properties.rhythmstring, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rhythm_version"]) -> typing.Union[MetaOapg.properties.rhythm_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["num_samples", "duration", "sample_md5", "offset_seconds", "window_seconds", "analysis_sample_rate", "analysis_channels", "end_of_fade_in", "start_of_fade_out", "loudness", "tempo", "tempo_confidence", "time_signature", "time_signature_confidence", "key", "key_confidence", "mode", "mode_confidence", "codestring", "code_version", "echoprintstring", "echoprint_version", "synchstring", "synch_version", "rhythmstring", "rhythm_version", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        num_samples: typing.Union[MetaOapg.properties.num_samples, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sample_md5: typing.Union[MetaOapg.properties.sample_md5, str, schemas.Unset] = schemas.unset,
        offset_seconds: typing.Union[MetaOapg.properties.offset_seconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        window_seconds: typing.Union[MetaOapg.properties.window_seconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        analysis_sample_rate: typing.Union[MetaOapg.properties.analysis_sample_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        analysis_channels: typing.Union[MetaOapg.properties.analysis_channels, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        end_of_fade_in: typing.Union[MetaOapg.properties.end_of_fade_in, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        start_of_fade_out: typing.Union[MetaOapg.properties.start_of_fade_out, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        loudness: typing.Union[MetaOapg.properties.loudness, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tempo: typing.Union[MetaOapg.properties.tempo, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tempo_confidence: typing.Union[MetaOapg.properties.tempo_confidence, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        time_signature: typing.Union['TimeSignature', schemas.Unset] = schemas.unset,
        time_signature_confidence: typing.Union[MetaOapg.properties.time_signature_confidence, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        key: typing.Union['Key', schemas.Unset] = schemas.unset,
        key_confidence: typing.Union[MetaOapg.properties.key_confidence, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        mode: typing.Union[MetaOapg.properties.mode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        mode_confidence: typing.Union[MetaOapg.properties.mode_confidence, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        codestring: typing.Union[MetaOapg.properties.codestring, str, schemas.Unset] = schemas.unset,
        code_version: typing.Union[MetaOapg.properties.code_version, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        echoprintstring: typing.Union[MetaOapg.properties.echoprintstring, str, schemas.Unset] = schemas.unset,
        echoprint_version: typing.Union[MetaOapg.properties.echoprint_version, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        synchstring: typing.Union[MetaOapg.properties.synchstring, str, schemas.Unset] = schemas.unset,
        synch_version: typing.Union[MetaOapg.properties.synch_version, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        rhythmstring: typing.Union[MetaOapg.properties.rhythmstring, str, schemas.Unset] = schemas.unset,
        rhythm_version: typing.Union[MetaOapg.properties.rhythm_version, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AudioAnalysisObjectTrack':
        return super().__new__(
            cls,
            *args,
            num_samples=num_samples,
            duration=duration,
            sample_md5=sample_md5,
            offset_seconds=offset_seconds,
            window_seconds=window_seconds,
            analysis_sample_rate=analysis_sample_rate,
            analysis_channels=analysis_channels,
            end_of_fade_in=end_of_fade_in,
            start_of_fade_out=start_of_fade_out,
            loudness=loudness,
            tempo=tempo,
            tempo_confidence=tempo_confidence,
            time_signature=time_signature,
            time_signature_confidence=time_signature_confidence,
            key=key,
            key_confidence=key_confidence,
            mode=mode,
            mode_confidence=mode_confidence,
            codestring=codestring,
            code_version=code_version,
            echoprintstring=echoprintstring,
            echoprint_version=echoprint_version,
            synchstring=synchstring,
            synch_version=synch_version,
            rhythmstring=rhythmstring,
            rhythm_version=rhythm_version,
            _configuration=_configuration,
            **kwargs,
        )

from spotify_python_sdk.model.key import Key
from spotify_python_sdk.model.time_signature import TimeSignature
