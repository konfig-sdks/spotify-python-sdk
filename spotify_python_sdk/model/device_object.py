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


class DeviceObject(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            is_active = schemas.BoolSchema
            is_private_session = schemas.BoolSchema
            is_restricted = schemas.BoolSchema
            name = schemas.StrSchema
            type = schemas.StrSchema
            
            
            class volume_percent(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 100
                    inclusive_minimum = 0
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'volume_percent':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            supports_volume = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "is_active": is_active,
                "is_private_session": is_private_session,
                "is_restricted": is_restricted,
                "name": name,
                "type": type,
                "volume_percent": volume_percent,
                "supports_volume": supports_volume,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_private_session"]) -> MetaOapg.properties.is_private_session: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_restricted"]) -> MetaOapg.properties.is_restricted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volume_percent"]) -> MetaOapg.properties.volume_percent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supports_volume"]) -> MetaOapg.properties.supports_volume: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "is_active", "is_private_session", "is_restricted", "name", "type", "volume_percent", "supports_volume", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_private_session"]) -> typing.Union[MetaOapg.properties.is_private_session, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_restricted"]) -> typing.Union[MetaOapg.properties.is_restricted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volume_percent"]) -> typing.Union[MetaOapg.properties.volume_percent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supports_volume"]) -> typing.Union[MetaOapg.properties.supports_volume, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "is_active", "is_private_session", "is_restricted", "name", "type", "volume_percent", "supports_volume", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, None, str, schemas.Unset] = schemas.unset,
        is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
        is_private_session: typing.Union[MetaOapg.properties.is_private_session, bool, schemas.Unset] = schemas.unset,
        is_restricted: typing.Union[MetaOapg.properties.is_restricted, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        volume_percent: typing.Union[MetaOapg.properties.volume_percent, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        supports_volume: typing.Union[MetaOapg.properties.supports_volume, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeviceObject':
        return super().__new__(
            cls,
            *args,
            id=id,
            is_active=is_active,
            is_private_session=is_private_session,
            is_restricted=is_restricted,
            name=name,
            type=type,
            volume_percent=volume_percent,
            supports_volume=supports_volume,
            _configuration=_configuration,
            **kwargs,
        )
