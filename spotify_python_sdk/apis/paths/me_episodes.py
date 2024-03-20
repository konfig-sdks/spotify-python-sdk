from spotify_python_sdk.paths.me_episodes.get import ApiForget
from spotify_python_sdk.paths.me_episodes.put import ApiForput
from spotify_python_sdk.paths.me_episodes.delete import ApiFordelete


class MeEpisodes(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
