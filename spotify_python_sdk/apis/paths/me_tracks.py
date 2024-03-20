from spotify_python_sdk.paths.me_tracks.get import ApiForget
from spotify_python_sdk.paths.me_tracks.put import ApiForput
from spotify_python_sdk.paths.me_tracks.delete import ApiFordelete


class MeTracks(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
