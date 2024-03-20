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


class TrackObject(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def album() -> typing.Type['SimplifiedAlbumObject']:
                return SimplifiedAlbumObject
            
            
            class artists(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ArtistObject']:
                        return ArtistObject
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ArtistObject'], typing.List['ArtistObject']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'artists':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ArtistObject':
                    return super().__getitem__(i)
        
            @staticmethod
            def available_markets() -> typing.Type['TrackObjectAvailableMarkets']:
                return TrackObjectAvailableMarkets
            disc_number = schemas.IntSchema
            duration_ms = schemas.IntSchema
            explicit = schemas.BoolSchema
        
            @staticmethod
            def external_ids() -> typing.Type['ExternalIdObject']:
                return ExternalIdObject
        
            @staticmethod
            def external_urls() -> typing.Type['ExternalUrlObject']:
                return ExternalUrlObject
            href = schemas.StrSchema
            id = schemas.StrSchema
            is_playable = schemas.BoolSchema
            linked_from = schemas.DictSchema
        
            @staticmethod
            def restrictions() -> typing.Type['TrackRestrictionObject']:
                return TrackRestrictionObject
            name = schemas.StrSchema
            popularity = schemas.IntSchema
            
            
            class preview_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'preview_url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            track_number = schemas.IntSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TRACK(cls):
                    return cls("track")
            uri = schemas.StrSchema
            is_local = schemas.BoolSchema
            __annotations__ = {
                "album": album,
                "artists": artists,
                "available_markets": available_markets,
                "disc_number": disc_number,
                "duration_ms": duration_ms,
                "explicit": explicit,
                "external_ids": external_ids,
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "is_playable": is_playable,
                "linked_from": linked_from,
                "restrictions": restrictions,
                "name": name,
                "popularity": popularity,
                "preview_url": preview_url,
                "track_number": track_number,
                "type": type,
                "uri": uri,
                "is_local": is_local,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["album"]) -> 'SimplifiedAlbumObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["artists"]) -> MetaOapg.properties.artists: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["available_markets"]) -> 'TrackObjectAvailableMarkets': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disc_number"]) -> MetaOapg.properties.disc_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_ms"]) -> MetaOapg.properties.duration_ms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["explicit"]) -> MetaOapg.properties.explicit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_ids"]) -> 'ExternalIdObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_urls"]) -> 'ExternalUrlObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_playable"]) -> MetaOapg.properties.is_playable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linked_from"]) -> MetaOapg.properties.linked_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restrictions"]) -> 'TrackRestrictionObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["popularity"]) -> MetaOapg.properties.popularity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preview_url"]) -> MetaOapg.properties.preview_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track_number"]) -> MetaOapg.properties.track_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_local"]) -> MetaOapg.properties.is_local: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["album", "artists", "available_markets", "disc_number", "duration_ms", "explicit", "external_ids", "external_urls", "href", "id", "is_playable", "linked_from", "restrictions", "name", "popularity", "preview_url", "track_number", "type", "uri", "is_local", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["album"]) -> typing.Union['SimplifiedAlbumObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["artists"]) -> typing.Union[MetaOapg.properties.artists, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["available_markets"]) -> typing.Union['TrackObjectAvailableMarkets', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disc_number"]) -> typing.Union[MetaOapg.properties.disc_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_ms"]) -> typing.Union[MetaOapg.properties.duration_ms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["explicit"]) -> typing.Union[MetaOapg.properties.explicit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_ids"]) -> typing.Union['ExternalIdObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_urls"]) -> typing.Union['ExternalUrlObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> typing.Union[MetaOapg.properties.href, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_playable"]) -> typing.Union[MetaOapg.properties.is_playable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linked_from"]) -> typing.Union[MetaOapg.properties.linked_from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restrictions"]) -> typing.Union['TrackRestrictionObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["popularity"]) -> typing.Union[MetaOapg.properties.popularity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preview_url"]) -> typing.Union[MetaOapg.properties.preview_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track_number"]) -> typing.Union[MetaOapg.properties.track_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> typing.Union[MetaOapg.properties.uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_local"]) -> typing.Union[MetaOapg.properties.is_local, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["album", "artists", "available_markets", "disc_number", "duration_ms", "explicit", "external_ids", "external_urls", "href", "id", "is_playable", "linked_from", "restrictions", "name", "popularity", "preview_url", "track_number", "type", "uri", "is_local", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        album: typing.Union['SimplifiedAlbumObject', schemas.Unset] = schemas.unset,
        artists: typing.Union[MetaOapg.properties.artists, list, tuple, schemas.Unset] = schemas.unset,
        available_markets: typing.Union['TrackObjectAvailableMarkets', schemas.Unset] = schemas.unset,
        disc_number: typing.Union[MetaOapg.properties.disc_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        duration_ms: typing.Union[MetaOapg.properties.duration_ms, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        explicit: typing.Union[MetaOapg.properties.explicit, bool, schemas.Unset] = schemas.unset,
        external_ids: typing.Union['ExternalIdObject', schemas.Unset] = schemas.unset,
        external_urls: typing.Union['ExternalUrlObject', schemas.Unset] = schemas.unset,
        href: typing.Union[MetaOapg.properties.href, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        is_playable: typing.Union[MetaOapg.properties.is_playable, bool, schemas.Unset] = schemas.unset,
        linked_from: typing.Union[MetaOapg.properties.linked_from, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        restrictions: typing.Union['TrackRestrictionObject', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        popularity: typing.Union[MetaOapg.properties.popularity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        preview_url: typing.Union[MetaOapg.properties.preview_url, None, str, schemas.Unset] = schemas.unset,
        track_number: typing.Union[MetaOapg.properties.track_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        uri: typing.Union[MetaOapg.properties.uri, str, schemas.Unset] = schemas.unset,
        is_local: typing.Union[MetaOapg.properties.is_local, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TrackObject':
        return super().__new__(
            cls,
            *args,
            album=album,
            artists=artists,
            available_markets=available_markets,
            disc_number=disc_number,
            duration_ms=duration_ms,
            explicit=explicit,
            external_ids=external_ids,
            external_urls=external_urls,
            href=href,
            id=id,
            is_playable=is_playable,
            linked_from=linked_from,
            restrictions=restrictions,
            name=name,
            popularity=popularity,
            preview_url=preview_url,
            track_number=track_number,
            type=type,
            uri=uri,
            is_local=is_local,
            _configuration=_configuration,
            **kwargs,
        )

from spotify_python_sdk.model.artist_object import ArtistObject
from spotify_python_sdk.model.external_id_object import ExternalIdObject
from spotify_python_sdk.model.external_url_object import ExternalUrlObject
from spotify_python_sdk.model.simplified_album_object import SimplifiedAlbumObject
from spotify_python_sdk.model.track_object_available_markets import TrackObjectAvailableMarkets
from spotify_python_sdk.model.track_restriction_object import TrackRestrictionObject
