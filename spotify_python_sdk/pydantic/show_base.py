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

from spotify_python_sdk.pydantic.copyright_object import CopyrightObject
from spotify_python_sdk.pydantic.external_url_object import ExternalUrlObject
from spotify_python_sdk.pydantic.image_object import ImageObject
from spotify_python_sdk.pydantic.show_base_available_markets import ShowBaseAvailableMarkets
from spotify_python_sdk.pydantic.show_base_languages import ShowBaseLanguages

class ShowBase(BaseModel):
    # A description of the show. HTML tags are stripped away from this field, use `html_description` field in case HTML tags are needed. 
    description: str = Field(alias='description')

    available_markets: ShowBaseAvailableMarkets = Field(alias='available_markets')

    # The copyright statements of the show. 
    copyrights: typing.List[CopyrightObject] = Field(alias='copyrights')

    # A description of the show. This field may contain HTML tags. 
    html_description: str = Field(alias='html_description')

    # Whether or not the show has explicit content (true = yes it does; false = no it does not OR unknown). 
    explicit: bool = Field(alias='explicit')

    # External URLs for this show. 
    external_urls: ExternalUrlObject = Field(alias='external_urls')

    # A link to the Web API endpoint providing full details of the show. 
    href: str = Field(alias='href')

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the show. 
    id: str = Field(alias='id')

    # The cover art for the show in various sizes, widest first. 
    images: typing.List[ImageObject] = Field(alias='images')

    # True if all of the shows episodes are hosted outside of Spotify's CDN. This field might be `null` in some cases. 
    is_externally_hosted: bool = Field(alias='is_externally_hosted')

    languages: ShowBaseLanguages = Field(alias='languages')

    # The media type of the show. 
    media_type: str = Field(alias='media_type')

    # The name of the episode. 
    name: str = Field(alias='name')

    # The publisher of the show. 
    publisher: str = Field(alias='publisher')

    # The object type. 
    type: Literal["show"] = Field(alias='type')

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the show. 
    uri: str = Field(alias='uri')

    # The total number of episodes in the show. 
    total_episodes: int = Field(alias='total_episodes')
    class Config:
        arbitrary_types_allowed = True
