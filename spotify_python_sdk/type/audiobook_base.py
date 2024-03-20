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

from spotify_python_sdk.type.audiobook_base_available_markets import AudiobookBaseAvailableMarkets
from spotify_python_sdk.type.audiobook_base_languages import AudiobookBaseLanguages
from spotify_python_sdk.type.author_object import AuthorObject
from spotify_python_sdk.type.copyright_object import CopyrightObject
from spotify_python_sdk.type.external_url_object import ExternalUrlObject
from spotify_python_sdk.type.image_object import ImageObject
from spotify_python_sdk.type.narrator_object import NarratorObject

class RequiredAudiobookBase(TypedDict):
    # A description of the audiobook. HTML tags are stripped away from this field, use `html_description` field in case HTML tags are needed. 
    description: str

    # The author(s) for the audiobook. 
    authors: typing.List[AuthorObject]

    available_markets: AudiobookBaseAvailableMarkets

    # The copyright statements of the audiobook. 
    copyrights: typing.List[CopyrightObject]

    # A description of the audiobook. This field may contain HTML tags. 
    html_description: str

    # Whether or not the audiobook has explicit content (true = yes it does; false = no it does not OR unknown). 
    explicit: bool

    # External URLs for this audiobook. 
    external_urls: ExternalUrlObject

    # A link to the Web API endpoint providing full details of the audiobook. 
    href: str

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the audiobook. 
    id: str

    # The cover art for the audiobook in various sizes, widest first. 
    images: typing.List[ImageObject]

    languages: AudiobookBaseLanguages

    # The media type of the audiobook. 
    media_type: str

    # The name of the audiobook. 
    name: str

    # The narrator(s) for the audiobook. 
    narrators: typing.List[NarratorObject]

    # The publisher of the audiobook. 
    publisher: str

    # The object type. 
    type: str

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the audiobook. 
    uri: str

    # The number of chapters in this audiobook. 
    total_chapters: int

class OptionalAudiobookBase(TypedDict, total=False):
    # The edition of the audiobook. 
    edition: str

class AudiobookBase(RequiredAudiobookBase, OptionalAudiobookBase):
    pass
