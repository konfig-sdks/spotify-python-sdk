from spotify_python_sdk.paths.me_shows.get import ApiForget
from spotify_python_sdk.paths.me_shows.put import ApiForput
from spotify_python_sdk.paths.me_shows.delete import ApiFordelete


class MeShows(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
