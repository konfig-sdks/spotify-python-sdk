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


class EpisodeBase(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "images",
            "languages",
            "description",
            "release_date_precision",
            "type",
            "html_description",
            "uri",
            "is_externally_hosted",
            "audio_preview_url",
            "duration_ms",
            "explicit",
            "is_playable",
            "resume_point",
            "release_date",
            "name",
            "href",
            "id",
            "external_urls",
        }
        
        class properties:
            description = schemas.StrSchema
            
            
            class audio_preview_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'audio_preview_url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            html_description = schemas.StrSchema
            duration_ms = schemas.IntSchema
            explicit = schemas.BoolSchema
        
            @staticmethod
            def external_urls() -> typing.Type['ExternalUrlObject']:
                return ExternalUrlObject
            href = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class images(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ImageObject']:
                        return ImageObject
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ImageObject'], typing.List['ImageObject']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'images':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ImageObject':
                    return super().__getitem__(i)
            is_externally_hosted = schemas.BoolSchema
            is_playable = schemas.BoolSchema
        
            @staticmethod
            def languages() -> typing.Type['EpisodeBaseLanguages']:
                return EpisodeBaseLanguages
            name = schemas.StrSchema
            release_date = schemas.StrSchema
            
            
            class release_date_precision(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("year")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("month")
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("day")
        
            @staticmethod
            def resume_point() -> typing.Type['ResumePointObject']:
                return ResumePointObject
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EPISODE(cls):
                    return cls("episode")
            uri = schemas.StrSchema
            language = schemas.StrSchema
        
            @staticmethod
            def restrictions() -> typing.Type['EpisodeRestrictionObject']:
                return EpisodeRestrictionObject
            __annotations__ = {
                "description": description,
                "audio_preview_url": audio_preview_url,
                "html_description": html_description,
                "duration_ms": duration_ms,
                "explicit": explicit,
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "images": images,
                "is_externally_hosted": is_externally_hosted,
                "is_playable": is_playable,
                "languages": languages,
                "name": name,
                "release_date": release_date,
                "release_date_precision": release_date_precision,
                "resume_point": resume_point,
                "type": type,
                "uri": uri,
                "language": language,
                "restrictions": restrictions,
            }
    
    images: MetaOapg.properties.images
    languages: 'EpisodeBaseLanguages'
    description: MetaOapg.properties.description
    release_date_precision: MetaOapg.properties.release_date_precision
    type: MetaOapg.properties.type
    html_description: MetaOapg.properties.html_description
    uri: MetaOapg.properties.uri
    is_externally_hosted: MetaOapg.properties.is_externally_hosted
    audio_preview_url: MetaOapg.properties.audio_preview_url
    duration_ms: MetaOapg.properties.duration_ms
    explicit: MetaOapg.properties.explicit
    is_playable: MetaOapg.properties.is_playable
    resume_point: 'ResumePointObject'
    release_date: MetaOapg.properties.release_date
    name: MetaOapg.properties.name
    href: MetaOapg.properties.href
    id: MetaOapg.properties.id
    external_urls: 'ExternalUrlObject'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audio_preview_url"]) -> MetaOapg.properties.audio_preview_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html_description"]) -> MetaOapg.properties.html_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_ms"]) -> MetaOapg.properties.duration_ms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["explicit"]) -> MetaOapg.properties.explicit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_urls"]) -> 'ExternalUrlObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["images"]) -> MetaOapg.properties.images: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_externally_hosted"]) -> MetaOapg.properties.is_externally_hosted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_playable"]) -> MetaOapg.properties.is_playable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["languages"]) -> 'EpisodeBaseLanguages': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["release_date"]) -> MetaOapg.properties.release_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["release_date_precision"]) -> MetaOapg.properties.release_date_precision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resume_point"]) -> 'ResumePointObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restrictions"]) -> 'EpisodeRestrictionObject': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "audio_preview_url", "html_description", "duration_ms", "explicit", "external_urls", "href", "id", "images", "is_externally_hosted", "is_playable", "languages", "name", "release_date", "release_date_precision", "resume_point", "type", "uri", "language", "restrictions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audio_preview_url"]) -> MetaOapg.properties.audio_preview_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html_description"]) -> MetaOapg.properties.html_description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_ms"]) -> MetaOapg.properties.duration_ms: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["explicit"]) -> MetaOapg.properties.explicit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_urls"]) -> 'ExternalUrlObject': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["images"]) -> MetaOapg.properties.images: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_externally_hosted"]) -> MetaOapg.properties.is_externally_hosted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_playable"]) -> MetaOapg.properties.is_playable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["languages"]) -> 'EpisodeBaseLanguages': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["release_date"]) -> MetaOapg.properties.release_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["release_date_precision"]) -> MetaOapg.properties.release_date_precision: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resume_point"]) -> 'ResumePointObject': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union[MetaOapg.properties.language, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restrictions"]) -> typing.Union['EpisodeRestrictionObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "audio_preview_url", "html_description", "duration_ms", "explicit", "external_urls", "href", "id", "images", "is_externally_hosted", "is_playable", "languages", "name", "release_date", "release_date_precision", "resume_point", "type", "uri", "language", "restrictions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        images: typing.Union[MetaOapg.properties.images, list, tuple, ],
        languages: 'EpisodeBaseLanguages',
        description: typing.Union[MetaOapg.properties.description, str, ],
        release_date_precision: typing.Union[MetaOapg.properties.release_date_precision, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        html_description: typing.Union[MetaOapg.properties.html_description, str, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        is_externally_hosted: typing.Union[MetaOapg.properties.is_externally_hosted, bool, ],
        audio_preview_url: typing.Union[MetaOapg.properties.audio_preview_url, None, str, ],
        duration_ms: typing.Union[MetaOapg.properties.duration_ms, decimal.Decimal, int, ],
        explicit: typing.Union[MetaOapg.properties.explicit, bool, ],
        is_playable: typing.Union[MetaOapg.properties.is_playable, bool, ],
        resume_point: 'ResumePointObject',
        release_date: typing.Union[MetaOapg.properties.release_date, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        href: typing.Union[MetaOapg.properties.href, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        external_urls: 'ExternalUrlObject',
        language: typing.Union[MetaOapg.properties.language, str, schemas.Unset] = schemas.unset,
        restrictions: typing.Union['EpisodeRestrictionObject', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EpisodeBase':
        return super().__new__(
            cls,
            *args,
            images=images,
            languages=languages,
            description=description,
            release_date_precision=release_date_precision,
            type=type,
            html_description=html_description,
            uri=uri,
            is_externally_hosted=is_externally_hosted,
            audio_preview_url=audio_preview_url,
            duration_ms=duration_ms,
            explicit=explicit,
            is_playable=is_playable,
            resume_point=resume_point,
            release_date=release_date,
            name=name,
            href=href,
            id=id,
            external_urls=external_urls,
            language=language,
            restrictions=restrictions,
            _configuration=_configuration,
            **kwargs,
        )

from spotify_python_sdk.model.episode_base_languages import EpisodeBaseLanguages
from spotify_python_sdk.model.episode_restriction_object import EpisodeRestrictionObject
from spotify_python_sdk.model.external_url_object import ExternalUrlObject
from spotify_python_sdk.model.image_object import ImageObject
from spotify_python_sdk.model.resume_point_object import ResumePointObject
