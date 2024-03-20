from spotify_python_sdk.paths.me_albums.get import ApiForget
from spotify_python_sdk.paths.me_albums.put import ApiForput
from spotify_python_sdk.paths.me_albums.delete import ApiFordelete


class MeAlbums(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
