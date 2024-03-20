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


class PrivateUserObject(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            country = schemas.StrSchema
            display_name = schemas.StrSchema
            email = schemas.StrSchema
        
            @staticmethod
            def explicit_content() -> typing.Type['ExplicitContentSettingsObject']:
                return ExplicitContentSettingsObject
        
            @staticmethod
            def external_urls() -> typing.Type['ExternalUrlObject']:
                return ExternalUrlObject
        
            @staticmethod
            def followers() -> typing.Type['FollowersObject']:
                return FollowersObject
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
            product = schemas.StrSchema
            type = schemas.StrSchema
            uri = schemas.StrSchema
            __annotations__ = {
                "country": country,
                "display_name": display_name,
                "email": email,
                "explicit_content": explicit_content,
                "external_urls": external_urls,
                "followers": followers,
                "href": href,
                "id": id,
                "images": images,
                "product": product,
                "type": type,
                "uri": uri,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["explicit_content"]) -> 'ExplicitContentSettingsObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_urls"]) -> 'ExternalUrlObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["followers"]) -> 'FollowersObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["images"]) -> MetaOapg.properties.images: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["product"]) -> MetaOapg.properties.product: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["country", "display_name", "email", "explicit_content", "external_urls", "followers", "href", "id", "images", "product", "type", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["explicit_content"]) -> typing.Union['ExplicitContentSettingsObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_urls"]) -> typing.Union['ExternalUrlObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["followers"]) -> typing.Union['FollowersObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> typing.Union[MetaOapg.properties.href, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["images"]) -> typing.Union[MetaOapg.properties.images, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["product"]) -> typing.Union[MetaOapg.properties.product, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> typing.Union[MetaOapg.properties.uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["country", "display_name", "email", "explicit_content", "external_urls", "followers", "href", "id", "images", "product", "type", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        explicit_content: typing.Union['ExplicitContentSettingsObject', schemas.Unset] = schemas.unset,
        external_urls: typing.Union['ExternalUrlObject', schemas.Unset] = schemas.unset,
        followers: typing.Union['FollowersObject', schemas.Unset] = schemas.unset,
        href: typing.Union[MetaOapg.properties.href, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        images: typing.Union[MetaOapg.properties.images, list, tuple, schemas.Unset] = schemas.unset,
        product: typing.Union[MetaOapg.properties.product, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        uri: typing.Union[MetaOapg.properties.uri, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PrivateUserObject':
        return super().__new__(
            cls,
            *args,
            country=country,
            display_name=display_name,
            email=email,
            explicit_content=explicit_content,
            external_urls=external_urls,
            followers=followers,
            href=href,
            id=id,
            images=images,
            product=product,
            type=type,
            uri=uri,
            _configuration=_configuration,
            **kwargs,
        )

from spotify_python_sdk.model.explicit_content_settings_object import ExplicitContentSettingsObject
from spotify_python_sdk.model.external_url_object import ExternalUrlObject
from spotify_python_sdk.model.followers_object import FollowersObject
from spotify_python_sdk.model.image_object import ImageObject
