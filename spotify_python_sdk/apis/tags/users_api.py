# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

from spotify_python_sdk.paths.me_following_contains.get import CheckFollowingArtistsUsers
from spotify_python_sdk.paths.playlists_playlist_id_followers_contains.get import CheckIfFollowsPlaylist
from spotify_python_sdk.paths.me_following.put import FollowArtistsOrUsers
from spotify_python_sdk.paths.playlists_playlist_id_followers.put import FollowPlaylist
from spotify_python_sdk.paths.me.get import GetCurrentUserProfile
from spotify_python_sdk.paths.me_following.get import GetFollowedArtists
from spotify_python_sdk.paths.me_top_type.get import GetTopItems
from spotify_python_sdk.paths.users_user_id_playlists.get import GetUserPlaylists
from spotify_python_sdk.paths.users_user_id.get import GetUserProfile
from spotify_python_sdk.paths.me_following.delete import UnfollowArtistsUsers
from spotify_python_sdk.paths.playlists_playlist_id_followers.delete import UnfollowPlaylist
from spotify_python_sdk.apis.tags.users_api_raw import UsersApiRaw


class UsersApi(
    CheckFollowingArtistsUsers,
    CheckIfFollowsPlaylist,
    FollowArtistsOrUsers,
    FollowPlaylist,
    GetCurrentUserProfile,
    GetFollowedArtists,
    GetTopItems,
    GetUserPlaylists,
    GetUserProfile,
    UnfollowArtistsUsers,
    UnfollowPlaylist,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UsersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UsersApiRaw(api_client)
