import typing_extensions

from spotify_python_sdk.apis.tags import TagValues
from spotify_python_sdk.apis.tags.library_api import LibraryApi
from spotify_python_sdk.apis.tags.tracks_api import TracksApi
from spotify_python_sdk.apis.tags.playlists_api import PlaylistsApi
from spotify_python_sdk.apis.tags.player_api import PlayerApi
from spotify_python_sdk.apis.tags.users_api import UsersApi
from spotify_python_sdk.apis.tags.albums_api import AlbumsApi
from spotify_python_sdk.apis.tags.artists_api import ArtistsApi
from spotify_python_sdk.apis.tags.audiobooks_api import AudiobooksApi
from spotify_python_sdk.apis.tags.episodes_api import EpisodesApi
from spotify_python_sdk.apis.tags.shows_api import ShowsApi
from spotify_python_sdk.apis.tags.categories_api import CategoriesApi
from spotify_python_sdk.apis.tags.chapters_api import ChaptersApi
from spotify_python_sdk.apis.tags.genres_api import GenresApi
from spotify_python_sdk.apis.tags.markets_api import MarketsApi
from spotify_python_sdk.apis.tags.search_api import SearchApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.LIBRARY: LibraryApi,
        TagValues.TRACKS: TracksApi,
        TagValues.PLAYLISTS: PlaylistsApi,
        TagValues.PLAYER: PlayerApi,
        TagValues.USERS: UsersApi,
        TagValues.ALBUMS: AlbumsApi,
        TagValues.ARTISTS: ArtistsApi,
        TagValues.AUDIOBOOKS: AudiobooksApi,
        TagValues.EPISODES: EpisodesApi,
        TagValues.SHOWS: ShowsApi,
        TagValues.CATEGORIES: CategoriesApi,
        TagValues.CHAPTERS: ChaptersApi,
        TagValues.GENRES: GenresApi,
        TagValues.MARKETS: MarketsApi,
        TagValues.SEARCH: SearchApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.LIBRARY: LibraryApi,
        TagValues.TRACKS: TracksApi,
        TagValues.PLAYLISTS: PlaylistsApi,
        TagValues.PLAYER: PlayerApi,
        TagValues.USERS: UsersApi,
        TagValues.ALBUMS: AlbumsApi,
        TagValues.ARTISTS: ArtistsApi,
        TagValues.AUDIOBOOKS: AudiobooksApi,
        TagValues.EPISODES: EpisodesApi,
        TagValues.SHOWS: ShowsApi,
        TagValues.CATEGORIES: CategoriesApi,
        TagValues.CHAPTERS: ChaptersApi,
        TagValues.GENRES: GenresApi,
        TagValues.MARKETS: MarketsApi,
        TagValues.SEARCH: SearchApi,
    }
)
