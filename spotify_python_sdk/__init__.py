# coding: utf-8

# flake8: noqa

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

__version__ = "1.0.0"

# import ApiClient
from spotify_python_sdk.api_client import ApiClient

# import Configuration
from spotify_python_sdk.configuration import Configuration

# import exceptions
from spotify_python_sdk.exceptions import OpenApiException
from spotify_python_sdk.exceptions import ApiAttributeError
from spotify_python_sdk.exceptions import ApiTypeError
from spotify_python_sdk.exceptions import ApiValueError
from spotify_python_sdk.exceptions import ApiKeyError
from spotify_python_sdk.exceptions import ApiException

from spotify_python_sdk.client import Spotify
