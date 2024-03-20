from spotify_python_sdk.paths.me_following.get import ApiForget
from spotify_python_sdk.paths.me_following.put import ApiForput
from spotify_python_sdk.paths.me_following.delete import ApiFordelete


class MeFollowing(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
