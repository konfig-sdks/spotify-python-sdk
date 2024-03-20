from spotify_python_sdk.paths.playlists_playlist_id_tracks.get import ApiForget
from spotify_python_sdk.paths.playlists_playlist_id_tracks.put import ApiForput
from spotify_python_sdk.paths.playlists_playlist_id_tracks.post import ApiForpost
from spotify_python_sdk.paths.playlists_playlist_id_tracks.delete import ApiFordelete


class PlaylistsPlaylistIdTracks(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
