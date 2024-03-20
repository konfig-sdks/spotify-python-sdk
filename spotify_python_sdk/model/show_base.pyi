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


class ShowBase(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "images",
            "languages",
            "copyrights",
            "available_markets",
            "description",
            "type",
            "html_description",
            "uri",
            "is_externally_hosted",
            "total_episodes",
            "explicit",
            "media_type",
            "name",
            "publisher",
            "href",
            "id",
            "external_urls",
        }
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def available_markets() -> typing.Type['ShowBaseAvailableMarkets']:
                return ShowBaseAvailableMarkets
            
            
            class copyrights(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CopyrightObject']:
                        return CopyrightObject
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CopyrightObject'], typing.List['CopyrightObject']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'copyrights':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CopyrightObject':
                    return super().__getitem__(i)
            html_description = schemas.StrSchema
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
        
            @staticmethod
            def languages() -> typing.Type['ShowBaseLanguages']:
                return ShowBaseLanguages
            media_type = schemas.StrSchema
            name = schemas.StrSchema
            publisher = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SHOW(cls):
                    return cls("show")
            uri = schemas.StrSchema
            total_episodes = schemas.IntSchema
            __annotations__ = {
                "description": description,
                "available_markets": available_markets,
                "copyrights": copyrights,
                "html_description": html_description,
                "explicit": explicit,
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "images": images,
                "is_externally_hosted": is_externally_hosted,
                "languages": languages,
                "media_type": media_type,
                "name": name,
                "publisher": publisher,
                "type": type,
                "uri": uri,
                "total_episodes": total_episodes,
            }
    
    images: MetaOapg.properties.images
    languages: 'ShowBaseLanguages'
    copyrights: MetaOapg.properties.copyrights
    available_markets: 'ShowBaseAvailableMarkets'
    description: MetaOapg.properties.description
    type: MetaOapg.properties.type
    html_description: MetaOapg.properties.html_description
    uri: MetaOapg.properties.uri
    is_externally_hosted: MetaOapg.properties.is_externally_hosted
    total_episodes: MetaOapg.properties.total_episodes
    explicit: MetaOapg.properties.explicit
    media_type: MetaOapg.properties.media_type
    name: MetaOapg.properties.name
    publisher: MetaOapg.properties.publisher
    href: MetaOapg.properties.href
    id: MetaOapg.properties.id
    external_urls: 'ExternalUrlObject'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["available_markets"]) -> 'ShowBaseAvailableMarkets': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyrights"]) -> MetaOapg.properties.copyrights: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html_description"]) -> MetaOapg.properties.html_description: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["languages"]) -> 'ShowBaseLanguages': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["media_type"]) -> MetaOapg.properties.media_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publisher"]) -> MetaOapg.properties.publisher: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_episodes"]) -> MetaOapg.properties.total_episodes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "available_markets", "copyrights", "html_description", "explicit", "external_urls", "href", "id", "images", "is_externally_hosted", "languages", "media_type", "name", "publisher", "type", "uri", "total_episodes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["available_markets"]) -> 'ShowBaseAvailableMarkets': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyrights"]) -> MetaOapg.properties.copyrights: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html_description"]) -> MetaOapg.properties.html_description: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["languages"]) -> 'ShowBaseLanguages': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["media_type"]) -> MetaOapg.properties.media_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publisher"]) -> MetaOapg.properties.publisher: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_episodes"]) -> MetaOapg.properties.total_episodes: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "available_markets", "copyrights", "html_description", "explicit", "external_urls", "href", "id", "images", "is_externally_hosted", "languages", "media_type", "name", "publisher", "type", "uri", "total_episodes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        images: typing.Union[MetaOapg.properties.images, list, tuple, ],
        languages: 'ShowBaseLanguages',
        copyrights: typing.Union[MetaOapg.properties.copyrights, list, tuple, ],
        available_markets: 'ShowBaseAvailableMarkets',
        description: typing.Union[MetaOapg.properties.description, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        html_description: typing.Union[MetaOapg.properties.html_description, str, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        is_externally_hosted: typing.Union[MetaOapg.properties.is_externally_hosted, bool, ],
        total_episodes: typing.Union[MetaOapg.properties.total_episodes, decimal.Decimal, int, ],
        explicit: typing.Union[MetaOapg.properties.explicit, bool, ],
        media_type: typing.Union[MetaOapg.properties.media_type, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        publisher: typing.Union[MetaOapg.properties.publisher, str, ],
        href: typing.Union[MetaOapg.properties.href, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        external_urls: 'ExternalUrlObject',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShowBase':
        return super().__new__(
            cls,
            *args,
            images=images,
            languages=languages,
            copyrights=copyrights,
            available_markets=available_markets,
            description=description,
            type=type,
            html_description=html_description,
            uri=uri,
            is_externally_hosted=is_externally_hosted,
            total_episodes=total_episodes,
            explicit=explicit,
            media_type=media_type,
            name=name,
            publisher=publisher,
            href=href,
            id=id,
            external_urls=external_urls,
            _configuration=_configuration,
            **kwargs,
        )

from spotify_python_sdk.model.copyright_object import CopyrightObject
from spotify_python_sdk.model.external_url_object import ExternalUrlObject
from spotify_python_sdk.model.image_object import ImageObject
from spotify_python_sdk.model.show_base_available_markets import ShowBaseAvailableMarkets
from spotify_python_sdk.model.show_base_languages import ShowBaseLanguages
