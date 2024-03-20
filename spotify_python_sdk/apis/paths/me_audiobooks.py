from spotify_python_sdk.paths.me_audiobooks.get import ApiForget
from spotify_python_sdk.paths.me_audiobooks.put import ApiForput
from spotify_python_sdk.paths.me_audiobooks.delete import ApiFordelete


class MeAudiobooks(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
