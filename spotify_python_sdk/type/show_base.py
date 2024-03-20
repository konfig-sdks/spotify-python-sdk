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

from spotify_python_sdk.type.copyright_object import CopyrightObject
from spotify_python_sdk.type.external_url_object import ExternalUrlObject
from spotify_python_sdk.type.image_object import ImageObject
from spotify_python_sdk.type.show_base_available_markets import ShowBaseAvailableMarkets
from spotify_python_sdk.type.show_base_languages import ShowBaseLanguages

class RequiredShowBase(TypedDict):
    # A description of the show. HTML tags are stripped away from this field, use `html_description` field in case HTML tags are needed. 
    description: str

    available_markets: ShowBaseAvailableMarkets

    # The copyright statements of the show. 
    copyrights: typing.List[CopyrightObject]

    # A description of the show. This field may contain HTML tags. 
    html_description: str

    # Whether or not the show has explicit content (true = yes it does; false = no it does not OR unknown). 
    explicit: bool

    # External URLs for this show. 
    external_urls: ExternalUrlObject

    # A link to the Web API endpoint providing full details of the show. 
    href: str

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the show. 
    id: str

    # The cover art for the show in various sizes, widest first. 
    images: typing.List[ImageObject]

    # True if all of the shows episodes are hosted outside of Spotify's CDN. This field might be `null` in some cases. 
    is_externally_hosted: bool

    languages: ShowBaseLanguages

    # The media type of the show. 
    media_type: str

    # The name of the episode. 
    name: str

    # The publisher of the show. 
    publisher: str

    # The object type. 
    type: str

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the show. 
    uri: str

    # The total number of episodes in the show. 
    total_episodes: int

class OptionalShowBase(TypedDict, total=False):
    pass

class ShowBase(RequiredShowBase, OptionalShowBase):
    pass
