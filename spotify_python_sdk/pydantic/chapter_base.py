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

from spotify_python_sdk.pydantic.chapter_base_available_markets import ChapterBaseAvailableMarkets
from spotify_python_sdk.pydantic.chapter_base_languages import ChapterBaseLanguages
from spotify_python_sdk.pydantic.chapter_restriction_object import ChapterRestrictionObject
from spotify_python_sdk.pydantic.external_url_object import ExternalUrlObject
from spotify_python_sdk.pydantic.image_object import ImageObject
from spotify_python_sdk.pydantic.resume_point_object import ResumePointObject

class ChapterBase(BaseModel):
    # A description of the chapter. HTML tags are stripped away from this field, use `html_description` field in case HTML tags are needed. 
    description: str = Field(alias='description')

    # A URL to a 30 second preview (MP3 format) of the chapter. `null` if not available. 
    audio_preview_url: typing.Optional[str] = Field(alias='audio_preview_url')

    # The number of the chapter 
    chapter_number: int = Field(alias='chapter_number')

    # A description of the chapter. This field may contain HTML tags. 
    html_description: str = Field(alias='html_description')

    # The chapter length in milliseconds. 
    duration_ms: int = Field(alias='duration_ms')

    # Whether or not the chapter has explicit content (true = yes it does; false = no it does not OR unknown). 
    explicit: bool = Field(alias='explicit')

    # External URLs for this chapter. 
    external_urls: ExternalUrlObject = Field(alias='external_urls')

    # A link to the Web API endpoint providing full details of the chapter. 
    href: str = Field(alias='href')

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the chapter. 
    id: str = Field(alias='id')

    # The cover art for the chapter in various sizes, widest first. 
    images: typing.List[ImageObject] = Field(alias='images')

    # True if the chapter is playable in the given market. Otherwise false. 
    is_playable: bool = Field(alias='is_playable')

    languages: ChapterBaseLanguages = Field(alias='languages')

    # The name of the chapter. 
    name: str = Field(alias='name')

    # The date the chapter was first released, for example `\"1981-12-15\"`. Depending on the precision, it might be shown as `\"1981\"` or `\"1981-12\"`. 
    release_date: str = Field(alias='release_date')

    # The precision with which `release_date` value is known. 
    release_date_precision: Literal["year", "month", "day"] = Field(alias='release_date_precision')

    # The user's most recent position in the chapter. Set if the supplied access token is a user token and has the scope 'user-read-playback-position'. 
    resume_point: ResumePointObject = Field(alias='resume_point')

    # The object type. 
    type: Literal["episode"] = Field(alias='type')

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the chapter. 
    uri: str = Field(alias='uri')

    available_markets: typing.Optional[ChapterBaseAvailableMarkets] = Field(None, alias='available_markets')

    # Included in the response when a content restriction is applied. 
    restrictions: typing.Optional[ChapterRestrictionObject] = Field(None, alias='restrictions')
    class Config:
        arbitrary_types_allowed = True
