# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

from spotify_python_sdk.paths.playlists_playlist_id_tracks.post import AddItems
from spotify_python_sdk.paths.me_tracks_contains.get import CheckSaved
from spotify_python_sdk.paths.audio_analysis_id.get import GetAudioAnalysis
from spotify_python_sdk.paths.audio_features_id.get import GetAudioFeaturesById
from spotify_python_sdk.paths.tracks_id.get import GetBySpotifyId
from spotify_python_sdk.paths.audio_features.get import GetMultipleAudioFeatures
from spotify_python_sdk.paths.tracks.get import GetMultipleByIds
from spotify_python_sdk.paths.playlists_playlist_id_tracks.get import GetPlaylistItems
from spotify_python_sdk.paths.recommendations.get import GetRecommendations
from spotify_python_sdk.paths.me_top_type.get import GetTopItems
from spotify_python_sdk.paths.artists_id_top_tracks.get import GetTopTracks
from spotify_python_sdk.paths.albums_id_tracks.get import GetTracksById
from spotify_python_sdk.paths.me_tracks.get import GetUserSaved
from spotify_python_sdk.paths.me_tracks.delete import RemoveFromLibrary
from spotify_python_sdk.paths.playlists_playlist_id_tracks.delete import RemoveItems
from spotify_python_sdk.paths.me_tracks.put import SaveForCurrentUser
from spotify_python_sdk.paths.playlists_playlist_id_tracks.put import UpdatePlaylistItems
from spotify_python_sdk.apis.tags.tracks_api_raw import TracksApiRaw


class TracksApi(
    AddItems,
    CheckSaved,
    GetAudioAnalysis,
    GetAudioFeaturesById,
    GetBySpotifyId,
    GetMultipleAudioFeatures,
    GetMultipleByIds,
    GetPlaylistItems,
    GetRecommendations,
    GetTopItems,
    GetTopTracks,
    GetTracksById,
    GetUserSaved,
    RemoveFromLibrary,
    RemoveItems,
    SaveForCurrentUser,
    UpdatePlaylistItems,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TracksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TracksApiRaw(api_client)
