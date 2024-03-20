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


class PlaylistObject(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            collaborative = schemas.BoolSchema
        
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
            name = schemas.StrSchema
        
            @staticmethod
            def owner() -> typing.Type['PlaylistOwnerObject']:
                return PlaylistOwnerObject
            public = schemas.BoolSchema
            snapshot_id = schemas.StrSchema
        
            @staticmethod
            def tracks() -> typing.Type['PagingPlaylistTrackObject']:
                return PagingPlaylistTrackObject
            type = schemas.StrSchema
            uri = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "collaborative": collaborative,
                "external_urls": external_urls,
                "followers": followers,
                "href": href,
                "id": id,
                "images": images,
                "name": name,
                "owner": owner,
                "public": public,
                "snapshot_id": snapshot_id,
                "tracks": tracks,
                "type": type,
                "uri": uri,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collaborative"]) -> MetaOapg.properties.collaborative: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> 'PlaylistOwnerObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public"]) -> MetaOapg.properties.public: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["snapshot_id"]) -> MetaOapg.properties.snapshot_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tracks"]) -> 'PagingPlaylistTrackObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "collaborative", "external_urls", "followers", "href", "id", "images", "name", "owner", "public", "snapshot_id", "tracks", "type", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collaborative"]) -> typing.Union[MetaOapg.properties.collaborative, schemas.Unset]: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union['PlaylistOwnerObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public"]) -> typing.Union[MetaOapg.properties.public, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["snapshot_id"]) -> typing.Union[MetaOapg.properties.snapshot_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tracks"]) -> typing.Union['PagingPlaylistTrackObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> typing.Union[MetaOapg.properties.uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "collaborative", "external_urls", "followers", "href", "id", "images", "name", "owner", "public", "snapshot_id", "tracks", "type", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        collaborative: typing.Union[MetaOapg.properties.collaborative, bool, schemas.Unset] = schemas.unset,
        external_urls: typing.Union['ExternalUrlObject', schemas.Unset] = schemas.unset,
        followers: typing.Union['FollowersObject', schemas.Unset] = schemas.unset,
        href: typing.Union[MetaOapg.properties.href, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        images: typing.Union[MetaOapg.properties.images, list, tuple, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        owner: typing.Union['PlaylistOwnerObject', schemas.Unset] = schemas.unset,
        public: typing.Union[MetaOapg.properties.public, bool, schemas.Unset] = schemas.unset,
        snapshot_id: typing.Union[MetaOapg.properties.snapshot_id, str, schemas.Unset] = schemas.unset,
        tracks: typing.Union['PagingPlaylistTrackObject', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        uri: typing.Union[MetaOapg.properties.uri, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PlaylistObject':
        return super().__new__(
            cls,
            *args,
            description=description,
            collaborative=collaborative,
            external_urls=external_urls,
            followers=followers,
            href=href,
            id=id,
            images=images,
            name=name,
            owner=owner,
            public=public,
            snapshot_id=snapshot_id,
            tracks=tracks,
            type=type,
            uri=uri,
            _configuration=_configuration,
            **kwargs,
        )

from spotify_python_sdk.model.external_url_object import ExternalUrlObject
from spotify_python_sdk.model.followers_object import FollowersObject
from spotify_python_sdk.model.image_object import ImageObject
from spotify_python_sdk.model.paging_playlist_track_object import PagingPlaylistTrackObject
from spotify_python_sdk.model.playlist_owner_object import PlaylistOwnerObject
