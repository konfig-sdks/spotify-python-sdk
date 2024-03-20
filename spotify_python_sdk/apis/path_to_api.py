import typing_extensions

from spotify_python_sdk.paths import PathValues
from spotify_python_sdk.apis.paths.albums_id import AlbumsId
from spotify_python_sdk.apis.paths.albums import Albums
from spotify_python_sdk.apis.paths.albums_id_tracks import AlbumsIdTracks
from spotify_python_sdk.apis.paths.artists_id import ArtistsId
from spotify_python_sdk.apis.paths.artists import Artists
from spotify_python_sdk.apis.paths.artists_id_albums import ArtistsIdAlbums
from spotify_python_sdk.apis.paths.artists_id_top_tracks import ArtistsIdTopTracks
from spotify_python_sdk.apis.paths.artists_id_related_artists import ArtistsIdRelatedArtists
from spotify_python_sdk.apis.paths.shows_id import ShowsId
from spotify_python_sdk.apis.paths.shows import Shows
from spotify_python_sdk.apis.paths.shows_id_episodes import ShowsIdEpisodes
from spotify_python_sdk.apis.paths.episodes_id import EpisodesId
from spotify_python_sdk.apis.paths.episodes import Episodes
from spotify_python_sdk.apis.paths.audiobooks_id import AudiobooksId
from spotify_python_sdk.apis.paths.audiobooks import Audiobooks
from spotify_python_sdk.apis.paths.audiobooks_id_chapters import AudiobooksIdChapters
from spotify_python_sdk.apis.paths.me_audiobooks import MeAudiobooks
from spotify_python_sdk.apis.paths.me_audiobooks_contains import MeAudiobooksContains
from spotify_python_sdk.apis.paths.chapters_id import ChaptersId
from spotify_python_sdk.apis.paths.chapters import Chapters
from spotify_python_sdk.apis.paths.tracks_id import TracksId
from spotify_python_sdk.apis.paths.tracks import Tracks
from spotify_python_sdk.apis.paths.search import Search
from spotify_python_sdk.apis.paths.me import Me
from spotify_python_sdk.apis.paths.playlists_playlist_id import PlaylistsPlaylistId
from spotify_python_sdk.apis.paths.playlists_playlist_id_tracks import PlaylistsPlaylistIdTracks
from spotify_python_sdk.apis.paths.me_playlists import MePlaylists
from spotify_python_sdk.apis.paths.me_albums import MeAlbums
from spotify_python_sdk.apis.paths.me_albums_contains import MeAlbumsContains
from spotify_python_sdk.apis.paths.me_tracks import MeTracks
from spotify_python_sdk.apis.paths.me_tracks_contains import MeTracksContains
from spotify_python_sdk.apis.paths.me_episodes import MeEpisodes
from spotify_python_sdk.apis.paths.me_episodes_contains import MeEpisodesContains
from spotify_python_sdk.apis.paths.me_shows import MeShows
from spotify_python_sdk.apis.paths.me_shows_contains import MeShowsContains
from spotify_python_sdk.apis.paths.me_top_type import MeTopType
from spotify_python_sdk.apis.paths.users_user_id import UsersUserId
from spotify_python_sdk.apis.paths.users_user_id_playlists import UsersUserIdPlaylists
from spotify_python_sdk.apis.paths.playlists_playlist_id_followers import PlaylistsPlaylistIdFollowers
from spotify_python_sdk.apis.paths.browse_featured_playlists import BrowseFeaturedPlaylists
from spotify_python_sdk.apis.paths.browse_categories import BrowseCategories
from spotify_python_sdk.apis.paths.browse_categories_category_id import BrowseCategoriesCategoryId
from spotify_python_sdk.apis.paths.browse_categories_category_id_playlists import BrowseCategoriesCategoryIdPlaylists
from spotify_python_sdk.apis.paths.playlists_playlist_id_images import PlaylistsPlaylistIdImages
from spotify_python_sdk.apis.paths.browse_new_releases import BrowseNewReleases
from spotify_python_sdk.apis.paths.me_following import MeFollowing
from spotify_python_sdk.apis.paths.me_following_contains import MeFollowingContains
from spotify_python_sdk.apis.paths.playlists_playlist_id_followers_contains import PlaylistsPlaylistIdFollowersContains
from spotify_python_sdk.apis.paths.audio_features import AudioFeatures
from spotify_python_sdk.apis.paths.audio_features_id import AudioFeaturesId
from spotify_python_sdk.apis.paths.audio_analysis_id import AudioAnalysisId
from spotify_python_sdk.apis.paths.recommendations import Recommendations
from spotify_python_sdk.apis.paths.recommendations_available_genre_seeds import RecommendationsAvailableGenreSeeds
from spotify_python_sdk.apis.paths.me_player import MePlayer
from spotify_python_sdk.apis.paths.me_player_devices import MePlayerDevices
from spotify_python_sdk.apis.paths.me_player_currently_playing import MePlayerCurrentlyPlaying
from spotify_python_sdk.apis.paths.me_player_play import MePlayerPlay
from spotify_python_sdk.apis.paths.me_player_pause import MePlayerPause
from spotify_python_sdk.apis.paths.me_player_next import MePlayerNext
from spotify_python_sdk.apis.paths.me_player_previous import MePlayerPrevious
from spotify_python_sdk.apis.paths.me_player_seek import MePlayerSeek
from spotify_python_sdk.apis.paths.me_player_repeat import MePlayerRepeat
from spotify_python_sdk.apis.paths.me_player_volume import MePlayerVolume
from spotify_python_sdk.apis.paths.me_player_shuffle import MePlayerShuffle
from spotify_python_sdk.apis.paths.me_player_recently_played import MePlayerRecentlyPlayed
from spotify_python_sdk.apis.paths.me_player_queue import MePlayerQueue
from spotify_python_sdk.apis.paths.markets import Markets

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ALBUMS_ID: AlbumsId,
        PathValues.ALBUMS: Albums,
        PathValues.ALBUMS_ID_TRACKS: AlbumsIdTracks,
        PathValues.ARTISTS_ID: ArtistsId,
        PathValues.ARTISTS: Artists,
        PathValues.ARTISTS_ID_ALBUMS: ArtistsIdAlbums,
        PathValues.ARTISTS_ID_TOPTRACKS: ArtistsIdTopTracks,
        PathValues.ARTISTS_ID_RELATEDARTISTS: ArtistsIdRelatedArtists,
        PathValues.SHOWS_ID: ShowsId,
        PathValues.SHOWS: Shows,
        PathValues.SHOWS_ID_EPISODES: ShowsIdEpisodes,
        PathValues.EPISODES_ID: EpisodesId,
        PathValues.EPISODES: Episodes,
        PathValues.AUDIOBOOKS_ID: AudiobooksId,
        PathValues.AUDIOBOOKS: Audiobooks,
        PathValues.AUDIOBOOKS_ID_CHAPTERS: AudiobooksIdChapters,
        PathValues.ME_AUDIOBOOKS: MeAudiobooks,
        PathValues.ME_AUDIOBOOKS_CONTAINS: MeAudiobooksContains,
        PathValues.CHAPTERS_ID: ChaptersId,
        PathValues.CHAPTERS: Chapters,
        PathValues.TRACKS_ID: TracksId,
        PathValues.TRACKS: Tracks,
        PathValues.SEARCH: Search,
        PathValues.ME: Me,
        PathValues.PLAYLISTS_PLAYLIST_ID: PlaylistsPlaylistId,
        PathValues.PLAYLISTS_PLAYLIST_ID_TRACKS: PlaylistsPlaylistIdTracks,
        PathValues.ME_PLAYLISTS: MePlaylists,
        PathValues.ME_ALBUMS: MeAlbums,
        PathValues.ME_ALBUMS_CONTAINS: MeAlbumsContains,
        PathValues.ME_TRACKS: MeTracks,
        PathValues.ME_TRACKS_CONTAINS: MeTracksContains,
        PathValues.ME_EPISODES: MeEpisodes,
        PathValues.ME_EPISODES_CONTAINS: MeEpisodesContains,
        PathValues.ME_SHOWS: MeShows,
        PathValues.ME_SHOWS_CONTAINS: MeShowsContains,
        PathValues.ME_TOP_TYPE: MeTopType,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_PLAYLISTS: UsersUserIdPlaylists,
        PathValues.PLAYLISTS_PLAYLIST_ID_FOLLOWERS: PlaylistsPlaylistIdFollowers,
        PathValues.BROWSE_FEATUREDPLAYLISTS: BrowseFeaturedPlaylists,
        PathValues.BROWSE_CATEGORIES: BrowseCategories,
        PathValues.BROWSE_CATEGORIES_CATEGORY_ID: BrowseCategoriesCategoryId,
        PathValues.BROWSE_CATEGORIES_CATEGORY_ID_PLAYLISTS: BrowseCategoriesCategoryIdPlaylists,
        PathValues.PLAYLISTS_PLAYLIST_ID_IMAGES: PlaylistsPlaylistIdImages,
        PathValues.BROWSE_NEWRELEASES: BrowseNewReleases,
        PathValues.ME_FOLLOWING: MeFollowing,
        PathValues.ME_FOLLOWING_CONTAINS: MeFollowingContains,
        PathValues.PLAYLISTS_PLAYLIST_ID_FOLLOWERS_CONTAINS: PlaylistsPlaylistIdFollowersContains,
        PathValues.AUDIOFEATURES: AudioFeatures,
        PathValues.AUDIOFEATURES_ID: AudioFeaturesId,
        PathValues.AUDIOANALYSIS_ID: AudioAnalysisId,
        PathValues.RECOMMENDATIONS: Recommendations,
        PathValues.RECOMMENDATIONS_AVAILABLEGENRESEEDS: RecommendationsAvailableGenreSeeds,
        PathValues.ME_PLAYER: MePlayer,
        PathValues.ME_PLAYER_DEVICES: MePlayerDevices,
        PathValues.ME_PLAYER_CURRENTLYPLAYING: MePlayerCurrentlyPlaying,
        PathValues.ME_PLAYER_PLAY: MePlayerPlay,
        PathValues.ME_PLAYER_PAUSE: MePlayerPause,
        PathValues.ME_PLAYER_NEXT: MePlayerNext,
        PathValues.ME_PLAYER_PREVIOUS: MePlayerPrevious,
        PathValues.ME_PLAYER_SEEK: MePlayerSeek,
        PathValues.ME_PLAYER_REPEAT: MePlayerRepeat,
        PathValues.ME_PLAYER_VOLUME: MePlayerVolume,
        PathValues.ME_PLAYER_SHUFFLE: MePlayerShuffle,
        PathValues.ME_PLAYER_RECENTLYPLAYED: MePlayerRecentlyPlayed,
        PathValues.ME_PLAYER_QUEUE: MePlayerQueue,
        PathValues.MARKETS: Markets,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ALBUMS_ID: AlbumsId,
        PathValues.ALBUMS: Albums,
        PathValues.ALBUMS_ID_TRACKS: AlbumsIdTracks,
        PathValues.ARTISTS_ID: ArtistsId,
        PathValues.ARTISTS: Artists,
        PathValues.ARTISTS_ID_ALBUMS: ArtistsIdAlbums,
        PathValues.ARTISTS_ID_TOPTRACKS: ArtistsIdTopTracks,
        PathValues.ARTISTS_ID_RELATEDARTISTS: ArtistsIdRelatedArtists,
        PathValues.SHOWS_ID: ShowsId,
        PathValues.SHOWS: Shows,
        PathValues.SHOWS_ID_EPISODES: ShowsIdEpisodes,
        PathValues.EPISODES_ID: EpisodesId,
        PathValues.EPISODES: Episodes,
        PathValues.AUDIOBOOKS_ID: AudiobooksId,
        PathValues.AUDIOBOOKS: Audiobooks,
        PathValues.AUDIOBOOKS_ID_CHAPTERS: AudiobooksIdChapters,
        PathValues.ME_AUDIOBOOKS: MeAudiobooks,
        PathValues.ME_AUDIOBOOKS_CONTAINS: MeAudiobooksContains,
        PathValues.CHAPTERS_ID: ChaptersId,
        PathValues.CHAPTERS: Chapters,
        PathValues.TRACKS_ID: TracksId,
        PathValues.TRACKS: Tracks,
        PathValues.SEARCH: Search,
        PathValues.ME: Me,
        PathValues.PLAYLISTS_PLAYLIST_ID: PlaylistsPlaylistId,
        PathValues.PLAYLISTS_PLAYLIST_ID_TRACKS: PlaylistsPlaylistIdTracks,
        PathValues.ME_PLAYLISTS: MePlaylists,
        PathValues.ME_ALBUMS: MeAlbums,
        PathValues.ME_ALBUMS_CONTAINS: MeAlbumsContains,
        PathValues.ME_TRACKS: MeTracks,
        PathValues.ME_TRACKS_CONTAINS: MeTracksContains,
        PathValues.ME_EPISODES: MeEpisodes,
        PathValues.ME_EPISODES_CONTAINS: MeEpisodesContains,
        PathValues.ME_SHOWS: MeShows,
        PathValues.ME_SHOWS_CONTAINS: MeShowsContains,
        PathValues.ME_TOP_TYPE: MeTopType,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_PLAYLISTS: UsersUserIdPlaylists,
        PathValues.PLAYLISTS_PLAYLIST_ID_FOLLOWERS: PlaylistsPlaylistIdFollowers,
        PathValues.BROWSE_FEATUREDPLAYLISTS: BrowseFeaturedPlaylists,
        PathValues.BROWSE_CATEGORIES: BrowseCategories,
        PathValues.BROWSE_CATEGORIES_CATEGORY_ID: BrowseCategoriesCategoryId,
        PathValues.BROWSE_CATEGORIES_CATEGORY_ID_PLAYLISTS: BrowseCategoriesCategoryIdPlaylists,
        PathValues.PLAYLISTS_PLAYLIST_ID_IMAGES: PlaylistsPlaylistIdImages,
        PathValues.BROWSE_NEWRELEASES: BrowseNewReleases,
        PathValues.ME_FOLLOWING: MeFollowing,
        PathValues.ME_FOLLOWING_CONTAINS: MeFollowingContains,
        PathValues.PLAYLISTS_PLAYLIST_ID_FOLLOWERS_CONTAINS: PlaylistsPlaylistIdFollowersContains,
        PathValues.AUDIOFEATURES: AudioFeatures,
        PathValues.AUDIOFEATURES_ID: AudioFeaturesId,
        PathValues.AUDIOANALYSIS_ID: AudioAnalysisId,
        PathValues.RECOMMENDATIONS: Recommendations,
        PathValues.RECOMMENDATIONS_AVAILABLEGENRESEEDS: RecommendationsAvailableGenreSeeds,
        PathValues.ME_PLAYER: MePlayer,
        PathValues.ME_PLAYER_DEVICES: MePlayerDevices,
        PathValues.ME_PLAYER_CURRENTLYPLAYING: MePlayerCurrentlyPlaying,
        PathValues.ME_PLAYER_PLAY: MePlayerPlay,
        PathValues.ME_PLAYER_PAUSE: MePlayerPause,
        PathValues.ME_PLAYER_NEXT: MePlayerNext,
        PathValues.ME_PLAYER_PREVIOUS: MePlayerPrevious,
        PathValues.ME_PLAYER_SEEK: MePlayerSeek,
        PathValues.ME_PLAYER_REPEAT: MePlayerRepeat,
        PathValues.ME_PLAYER_VOLUME: MePlayerVolume,
        PathValues.ME_PLAYER_SHUFFLE: MePlayerShuffle,
        PathValues.ME_PLAYER_RECENTLYPLAYED: MePlayerRecentlyPlayed,
        PathValues.ME_PLAYER_QUEUE: MePlayerQueue,
        PathValues.MARKETS: Markets,
    }
)
