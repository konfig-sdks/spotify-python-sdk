# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from spotify_python_sdk.pydantic.explicit_content_settings_object import ExplicitContentSettingsObject
from spotify_python_sdk.pydantic.external_url_object import ExternalUrlObject
from spotify_python_sdk.pydantic.followers_object import FollowersObject
from spotify_python_sdk.pydantic.image_object import ImageObject

class PrivateUserObject(BaseModel):
    # The country of the user, as set in the user's account profile. An [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). _This field is only available when the current user has granted access to the [user-read-private](/documentation/web-api/concepts/scopes/#list-of-scopes) scope._ 
    country: typing.Optional[str] = Field(None, alias='country')

    # The name displayed on the user's profile. `null` if not available. 
    display_name: typing.Optional[str] = Field(None, alias='display_name')

    # The user's email address, as entered by the user when creating their account. _**Important!** This email address is unverified; there is no proof that it actually belongs to the user._ _This field is only available when the current user has granted access to the [user-read-email](/documentation/web-api/concepts/scopes/#list-of-scopes) scope._ 
    email: typing.Optional[str] = Field(None, alias='email')

    # The user's explicit content settings. _This field is only available when the current user has granted access to the [user-read-private](/documentation/web-api/concepts/scopes/#list-of-scopes) scope._ 
    explicit_content: typing.Optional[ExplicitContentSettingsObject] = Field(None, alias='explicit_content')

    # Known external URLs for this user.
    external_urls: typing.Optional[ExternalUrlObject] = Field(None, alias='external_urls')

    # Information about the followers of the user.
    followers: typing.Optional[FollowersObject] = Field(None, alias='followers')

    # A link to the Web API endpoint for this user. 
    href: typing.Optional[str] = Field(None, alias='href')

    # The [Spotify user ID](/documentation/web-api/concepts/spotify-uris-ids) for the user. 
    id: typing.Optional[str] = Field(None, alias='id')

    # The user's profile image.
    images: typing.Optional[typing.List[ImageObject]] = Field(None, alias='images')

    # The user's Spotify subscription level: \"premium\", \"free\", etc. (The subscription level \"open\" can be considered the same as \"free\".) _This field is only available when the current user has granted access to the [user-read-private](/documentation/web-api/concepts/scopes/#list-of-scopes) scope._ 
    product: typing.Optional[str] = Field(None, alias='product')

    # The object type: \"user\" 
    type: typing.Optional[str] = Field(None, alias='type')

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the user. 
    uri: typing.Optional[str] = Field(None, alias='uri')
    class Config:
        arbitrary_types_allowed = True
