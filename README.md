<div align="left">

[![Visit Spotify](./header.png)](https://developer.spotify.com)

# Spotify<a id="spotify"></a>

You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.

In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.

The base URI for all Web API requests is `https://api.spotify.com/v1`.

Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`spotify.albums.check_saved`](#spotifyalbumscheck_saved)
  * [`spotify.albums.get_albums_by_id`](#spotifyalbumsget_albums_by_id)
  * [`spotify.albums.get_information`](#spotifyalbumsget_information)
  * [`spotify.albums.get_new_releases`](#spotifyalbumsget_new_releases)
  * [`spotify.albums.get_saved`](#spotifyalbumsget_saved)
  * [`spotify.albums.get_tracks_by_id`](#spotifyalbumsget_tracks_by_id)
  * [`spotify.albums.list_several`](#spotifyalbumslist_several)
  * [`spotify.albums.remove_saved`](#spotifyalbumsremove_saved)
  * [`spotify.albums.save_current_user_library`](#spotifyalbumssave_current_user_library)
  * [`spotify.artists.check_following_artists_users`](#spotifyartistscheck_following_artists_users)
  * [`spotify.artists.follow_artists_or_users`](#spotifyartistsfollow_artists_or_users)
  * [`spotify.artists.get_albums_by_id`](#spotifyartistsget_albums_by_id)
  * [`spotify.artists.get_catalog_info`](#spotifyartistsget_catalog_info)
  * [`spotify.artists.get_catalog_info_0`](#spotifyartistsget_catalog_info_0)
  * [`spotify.artists.get_followed_artists`](#spotifyartistsget_followed_artists)
  * [`spotify.artists.get_related_artists`](#spotifyartistsget_related_artists)
  * [`spotify.artists.get_top_tracks`](#spotifyartistsget_top_tracks)
  * [`spotify.artists.unfollow_artists_users`](#spotifyartistsunfollow_artists_users)
  * [`spotify.audiobooks.check_user_saved`](#spotifyaudiobookscheck_user_saved)
  * [`spotify.audiobooks.get_catalog_info`](#spotifyaudiobooksget_catalog_info)
  * [`spotify.audiobooks.get_chapters_by_id`](#spotifyaudiobooksget_chapters_by_id)
  * [`spotify.audiobooks.get_several`](#spotifyaudiobooksget_several)
  * [`spotify.audiobooks.list_saved`](#spotifyaudiobookslist_saved)
  * [`spotify.audiobooks.remove_from_library`](#spotifyaudiobooksremove_from_library)
  * [`spotify.audiobooks.save_current_user_library`](#spotifyaudiobookssave_current_user_library)
  * [`spotify.categories.get_category_playlists`](#spotifycategoriesget_category_playlists)
  * [`spotify.categories.get_single`](#spotifycategoriesget_single)
  * [`spotify.categories.list_several`](#spotifycategorieslist_several)
  * [`spotify.chapters.get_chapter_info`](#spotifychaptersget_chapter_info)
  * [`spotify.chapters.get_chapters_by_id`](#spotifychaptersget_chapters_by_id)
  * [`spotify.chapters.get_multiple_by_ids`](#spotifychaptersget_multiple_by_ids)
  * [`spotify.episodes.check_saved_episodes`](#spotifyepisodescheck_saved_episodes)
  * [`spotify.episodes.get_episodes_by_id`](#spotifyepisodesget_episodes_by_id)
  * [`spotify.episodes.get_several`](#spotifyepisodesget_several)
  * [`spotify.episodes.get_single_by_id`](#spotifyepisodesget_single_by_id)
  * [`spotify.episodes.get_user_saved_episodes`](#spotifyepisodesget_user_saved_episodes)
  * [`spotify.episodes.remove_from_library`](#spotifyepisodesremove_from_library)
  * [`spotify.episodes.save_current_user_library`](#spotifyepisodessave_current_user_library)
  * [`spotify.genres.get_available_seeds`](#spotifygenresget_available_seeds)
  * [`spotify.library.check_following_artists_users`](#spotifylibrarycheck_following_artists_users)
  * [`spotify.library.check_saved`](#spotifylibrarycheck_saved)
  * [`spotify.library.check_saved_0`](#spotifylibrarycheck_saved_0)
  * [`spotify.library.check_saved_episodes`](#spotifylibrarycheck_saved_episodes)
  * [`spotify.library.check_saved_shows`](#spotifylibrarycheck_saved_shows)
  * [`spotify.library.check_user_saved`](#spotifylibrarycheck_user_saved)
  * [`spotify.library.create_playlist`](#spotifylibrarycreate_playlist)
  * [`spotify.library.follow_artists_or_users`](#spotifylibraryfollow_artists_or_users)
  * [`spotify.library.get_followed_artists`](#spotifylibraryget_followed_artists)
  * [`spotify.library.get_saved`](#spotifylibraryget_saved)
  * [`spotify.library.get_top_items`](#spotifylibraryget_top_items)
  * [`spotify.library.get_user_playlists`](#spotifylibraryget_user_playlists)
  * [`spotify.library.get_user_saved`](#spotifylibraryget_user_saved)
  * [`spotify.library.get_user_saved_episodes`](#spotifylibraryget_user_saved_episodes)
  * [`spotify.library.get_user_saved_shows`](#spotifylibraryget_user_saved_shows)
  * [`spotify.library.list_saved`](#spotifylibrarylist_saved)
  * [`spotify.library.remove_from_library`](#spotifylibraryremove_from_library)
  * [`spotify.library.remove_from_library_0`](#spotifylibraryremove_from_library_0)
  * [`spotify.library.remove_from_library_1`](#spotifylibraryremove_from_library_1)
  * [`spotify.library.remove_saved`](#spotifylibraryremove_saved)
  * [`spotify.library.remove_user_library`](#spotifylibraryremove_user_library)
  * [`spotify.library.save_current_user_library`](#spotifylibrarysave_current_user_library)
  * [`spotify.library.save_current_user_library_0`](#spotifylibrarysave_current_user_library_0)
  * [`spotify.library.save_current_user_library_1`](#spotifylibrarysave_current_user_library_1)
  * [`spotify.library.save_current_user_library_2`](#spotifylibrarysave_current_user_library_2)
  * [`spotify.library.save_for_current_user`](#spotifylibrarysave_for_current_user)
  * [`spotify.library.unfollow_artists_users`](#spotifylibraryunfollow_artists_users)
  * [`spotify.library.update_details`](#spotifylibraryupdate_details)
  * [`spotify.markets.list_available`](#spotifymarketslist_available)
  * [`spotify.player.add_item_to_queue`](#spotifyplayeradd_item_to_queue)
  * [`spotify.player.get_available_devices`](#spotifyplayerget_available_devices)
  * [`spotify.player.get_current_playback_state`](#spotifyplayerget_current_playback_state)
  * [`spotify.player.get_currently_playing_track`](#spotifyplayerget_currently_playing_track)
  * [`spotify.player.get_recently_played_tracks`](#spotifyplayerget_recently_played_tracks)
  * [`spotify.player.get_user_queue`](#spotifyplayerget_user_queue)
  * [`spotify.player.pause_playback`](#spotifyplayerpause_playback)
  * [`spotify.player.seek_to_position`](#spotifyplayerseek_to_position)
  * [`spotify.player.set_playback_volume`](#spotifyplayerset_playback_volume)
  * [`spotify.player.set_repeat_mode`](#spotifyplayerset_repeat_mode)
  * [`spotify.player.skip_to_next_track`](#spotifyplayerskip_to_next_track)
  * [`spotify.player.skip_to_previous_track`](#spotifyplayerskip_to_previous_track)
  * [`spotify.player.start_playback`](#spotifyplayerstart_playback)
  * [`spotify.player.toggle_playback_shuffle`](#spotifyplayertoggle_playback_shuffle)
  * [`spotify.player.transfer_playback_to_new_device`](#spotifyplayertransfer_playback_to_new_device)
  * [`spotify.playlists.add_items`](#spotifyplaylistsadd_items)
  * [`spotify.playlists.check_if_follows_playlist`](#spotifyplaylistscheck_if_follows_playlist)
  * [`spotify.playlists.create_playlist`](#spotifyplaylistscreate_playlist)
  * [`spotify.playlists.follow_playlist`](#spotifyplaylistsfollow_playlist)
  * [`spotify.playlists.get_category_playlists`](#spotifyplaylistsget_category_playlists)
  * [`spotify.playlists.get_cover_image`](#spotifyplaylistsget_cover_image)
  * [`spotify.playlists.get_featured`](#spotifyplaylistsget_featured)
  * [`spotify.playlists.get_playlist_by_id`](#spotifyplaylistsget_playlist_by_id)
  * [`spotify.playlists.get_playlist_items`](#spotifyplaylistsget_playlist_items)
  * [`spotify.playlists.get_user_playlists`](#spotifyplaylistsget_user_playlists)
  * [`spotify.playlists.get_user_playlists_0`](#spotifyplaylistsget_user_playlists_0)
  * [`spotify.playlists.remove_items`](#spotifyplaylistsremove_items)
  * [`spotify.playlists.replace_cover_image`](#spotifyplaylistsreplace_cover_image)
  * [`spotify.playlists.unfollow_playlist`](#spotifyplaylistsunfollow_playlist)
  * [`spotify.playlists.update_details`](#spotifyplaylistsupdate_details)
  * [`spotify.playlists.update_playlist_items`](#spotifyplaylistsupdate_playlist_items)
  * [`spotify.search.spotify_catalog_info`](#spotifysearchspotify_catalog_info)
  * [`spotify.shows.check_saved_shows`](#spotifyshowscheck_saved_shows)
  * [`spotify.shows.get_episodes_by_id`](#spotifyshowsget_episodes_by_id)
  * [`spotify.shows.get_information`](#spotifyshowsget_information)
  * [`spotify.shows.get_multiple_shows_info`](#spotifyshowsget_multiple_shows_info)
  * [`spotify.shows.get_user_saved_shows`](#spotifyshowsget_user_saved_shows)
  * [`spotify.shows.remove_user_library`](#spotifyshowsremove_user_library)
  * [`spotify.shows.save_current_user_library`](#spotifyshowssave_current_user_library)
  * [`spotify.tracks.add_items`](#spotifytracksadd_items)
  * [`spotify.tracks.check_saved`](#spotifytrackscheck_saved)
  * [`spotify.tracks.get_audio_analysis`](#spotifytracksget_audio_analysis)
  * [`spotify.tracks.get_audio_features_by_id`](#spotifytracksget_audio_features_by_id)
  * [`spotify.tracks.get_by_spotify_id`](#spotifytracksget_by_spotify_id)
  * [`spotify.tracks.get_multiple_audio_features`](#spotifytracksget_multiple_audio_features)
  * [`spotify.tracks.get_multiple_by_ids`](#spotifytracksget_multiple_by_ids)
  * [`spotify.tracks.get_playlist_items`](#spotifytracksget_playlist_items)
  * [`spotify.tracks.get_recommendations`](#spotifytracksget_recommendations)
  * [`spotify.tracks.get_top_items`](#spotifytracksget_top_items)
  * [`spotify.tracks.get_top_tracks`](#spotifytracksget_top_tracks)
  * [`spotify.tracks.get_tracks_by_id`](#spotifytracksget_tracks_by_id)
  * [`spotify.tracks.get_user_saved`](#spotifytracksget_user_saved)
  * [`spotify.tracks.remove_from_library`](#spotifytracksremove_from_library)
  * [`spotify.tracks.remove_items`](#spotifytracksremove_items)
  * [`spotify.tracks.save_for_current_user`](#spotifytrackssave_for_current_user)
  * [`spotify.tracks.update_playlist_items`](#spotifytracksupdate_playlist_items)
  * [`spotify.users.check_following_artists_users`](#spotifyuserscheck_following_artists_users)
  * [`spotify.users.check_if_follows_playlist`](#spotifyuserscheck_if_follows_playlist)
  * [`spotify.users.follow_artists_or_users`](#spotifyusersfollow_artists_or_users)
  * [`spotify.users.follow_playlist`](#spotifyusersfollow_playlist)
  * [`spotify.users.get_current_user_profile`](#spotifyusersget_current_user_profile)
  * [`spotify.users.get_followed_artists`](#spotifyusersget_followed_artists)
  * [`spotify.users.get_top_items`](#spotifyusersget_top_items)
  * [`spotify.users.get_user_playlists`](#spotifyusersget_user_playlists)
  * [`spotify.users.get_user_profile`](#spotifyusersget_user_profile)
  * [`spotify.users.unfollow_artists_users`](#spotifyusersunfollow_artists_users)
  * [`spotify.users.unfollow_playlist`](#spotifyusersunfollow_playlist)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Spotify&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from spotify_python_sdk import Spotify, ApiException

spotify = Spotify(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Check User's Saved Albums 
    check_saved_response = spotify.albums.check_saved(
        ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
    )
    print(check_saved_response)
except ApiException as e:
    print("Exception when calling AlbumsApi.check_saved: %s\n" % e)
    pprint(e.body)
    if e.status == 401:
        pprint(e.body["error"])
    if e.status == 403:
        pprint(e.body["error"])
    if e.status == 429:
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from spotify_python_sdk import Spotify, ApiException

spotify = Spotify(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Check User's Saved Albums 
        check_saved_response = await spotify.albums.acheck_saved(
            ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
        )
        print(check_saved_response)
    except ApiException as e:
        print("Exception when calling AlbumsApi.check_saved: %s\n" % e)
        pprint(e.body)
        if e.status == 401:
            pprint(e.body["error"])
        if e.status == 403:
            pprint(e.body["error"])
        if e.status == 429:
            pprint(e.body["error"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from spotify_python_sdk import Spotify, ApiException

spotify = Spotify(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Check User's Saved Albums 
    check_saved_response = spotify.albums.raw.check_saved(
        ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
    )
    pprint(check_saved_response.body)
    pprint(check_saved_response.headers)
    pprint(check_saved_response.status)
    pprint(check_saved_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AlbumsApi.check_saved: %s\n" % e)
    pprint(e.body)
    if e.status == 401:
        pprint(e.body["error"])
    if e.status == 403:
        pprint(e.body["error"])
    if e.status == 429:
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `spotify.albums.check_saved`<a id="spotifyalbumscheck_saved"></a>

Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_saved_response = spotify.albums.check_saved(
    ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/albums/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.albums.get_albums_by_id`<a id="spotifyalbumsget_albums_by_id"></a>

Get Spotify catalog information about an artist's albums.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_albums_by_id_response = spotify.albums.get_albums_by_id(
    id="0TnOYISbd1XYRBk9myaseg",
    include_groups="single,appears_on",
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### include_groups: `str`<a id="include_groups-str"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingArtistDiscographyAlbumObject`](./spotify_python_sdk/pydantic/paging_artist_discography_album_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/artists/{id}/albums` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.albums.get_information`<a id="spotifyalbumsget_information"></a>

Get Spotify catalog information for a single album.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = spotify.albums.get_information(
    id="4aawyAB9vmqN3uQ7FjRGTy",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AlbumObject`](./spotify_python_sdk/pydantic/album_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/albums/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.albums.get_new_releases`<a id="spotifyalbumsget_new_releases"></a>

Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_new_releases_response = spotify.albums.get_new_releases(
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AlbumsGetNewReleasesResponse`](./spotify_python_sdk/pydantic/albums_get_new_releases_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/browse/new-releases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.albums.get_saved`<a id="spotifyalbumsget_saved"></a>

Get a list of the albums saved in the current Spotify user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_saved_response = spotify.albums.get_saved(
    limit=10,
    offset=5,
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSavedAlbumObject`](./spotify_python_sdk/pydantic/paging_saved_album_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/albums` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.albums.get_tracks_by_id`<a id="spotifyalbumsget_tracks_by_id"></a>

Get Spotify catalog information about an album’s tracks.
Optional parameters can be used to limit the number of tracks returned.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tracks_by_id_response = spotify.albums.get_tracks_by_id(
    id="4aawyAB9vmqN3uQ7FjRGTy",
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSimplifiedTrackObject`](./spotify_python_sdk/pydantic/paging_simplified_track_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/albums/{id}/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.albums.list_several`<a id="spotifyalbumslist_several"></a>

Get Spotify catalog information for multiple albums identified by their Spotify IDs.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_several_response = spotify.albums.list_several(
    ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AlbumsListSeveralResponse`](./spotify_python_sdk/pydantic/albums_list_several_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/albums` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.albums.remove_saved`<a id="spotifyalbumsremove_saved"></a>

Remove one or more albums from the current user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.albums.remove_saved(
    ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`AlbumsRemoveSavedRequest`](./spotify_python_sdk/type/albums_remove_saved_request.py)<a id="requestbody-albumsremovesavedrequestspotify_python_sdktypealbums_remove_saved_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/albums` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.albums.save_current_user_library`<a id="spotifyalbumssave_current_user_library"></a>

Save one or more albums to the current user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.albums.save_current_user_library(
    ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`AlbumsSaveCurrentUserLibraryRequest`](./spotify_python_sdk/type/albums_save_current_user_library_request.py)<a id="requestbody-albumssavecurrentuserlibraryrequestspotify_python_sdktypealbums_save_current_user_library_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/albums` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.artists.check_following_artists_users`<a id="spotifyartistscheck_following_artists_users"></a>

Check to see if the current user is following one or more artists or other Spotify users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_following_artists_users_response = spotify.artists.check_following_artists_users(
    type="artist",
    ids="2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.artists.follow_artists_or_users`<a id="spotifyartistsfollow_artists_or_users"></a>

Add the current user as a follower of one or more artists or other Spotify users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.artists.follow_artists_or_users(
    ids=[
        "string_example"
    ],
    type="artist",
    ids="2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`UsersFollowArtistsOrUsersRequest`](./spotify_python_sdk/type/users_follow_artists_or_users_request.py)<a id="requestbody-usersfollowartistsorusersrequestspotify_python_sdktypeusers_follow_artists_or_users_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.artists.get_albums_by_id`<a id="spotifyartistsget_albums_by_id"></a>

Get Spotify catalog information about an artist's albums.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_albums_by_id_response = spotify.artists.get_albums_by_id(
    id="0TnOYISbd1XYRBk9myaseg",
    include_groups="single,appears_on",
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### include_groups: `str`<a id="include_groups-str"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingArtistDiscographyAlbumObject`](./spotify_python_sdk/pydantic/paging_artist_discography_album_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/artists/{id}/albums` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.artists.get_catalog_info`<a id="spotifyartistsget_catalog_info"></a>

Get Spotify catalog information for a single artist identified by their unique Spotify ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_catalog_info_response = spotify.artists.get_catalog_info(
    id="0TnOYISbd1XYRBk9myaseg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ArtistObject`](./spotify_python_sdk/pydantic/artist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/artists/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.artists.get_catalog_info_0`<a id="spotifyartistsget_catalog_info_0"></a>

Get Spotify catalog information for several artists based on their Spotify IDs.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_catalog_info_0_response = spotify.artists.get_catalog_info_0(
    ids="2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ArtistsGetCatalogInfoResponse`](./spotify_python_sdk/pydantic/artists_get_catalog_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/artists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.artists.get_followed_artists`<a id="spotifyartistsget_followed_artists"></a>

Get the current user's followed artists.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_followed_artists_response = spotify.artists.get_followed_artists(
    type="artist",
    after="0I2XqVXqHScXjHhk6AYYRe",
    limit=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetFollowedArtistsResponse`](./spotify_python_sdk/pydantic/users_get_followed_artists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.artists.get_related_artists`<a id="spotifyartistsget_related_artists"></a>

Get Spotify catalog information about artists similar to a given artist. Similarity is based on analysis of the Spotify community's listening history.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_related_artists_response = spotify.artists.get_related_artists(
    id="0TnOYISbd1XYRBk9myaseg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ArtistsGetCatalogInfoResponse`](./spotify_python_sdk/pydantic/artists_get_catalog_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/artists/{id}/related-artists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.artists.get_top_tracks`<a id="spotifyartistsget_top_tracks"></a>

Get Spotify catalog information about an artist's top tracks by country.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_top_tracks_response = spotify.artists.get_top_tracks(
    id="0TnOYISbd1XYRBk9myaseg",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ArtistsGetTopTracksResponse`](./spotify_python_sdk/pydantic/artists_get_top_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/artists/{id}/top-tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.artists.unfollow_artists_users`<a id="spotifyartistsunfollow_artists_users"></a>

Remove the current user as a follower of one or more artists or other Spotify users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.artists.unfollow_artists_users(
    type="artist",
    ids="2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`UsersUnfollowArtistsUsersRequest`](./spotify_python_sdk/type/users_unfollow_artists_users_request.py)<a id="requestbody-usersunfollowartistsusersrequestspotify_python_sdktypeusers_unfollow_artists_users_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.audiobooks.check_user_saved`<a id="spotifyaudiobookscheck_user_saved"></a>

Check if one or more audiobooks are already saved in the current Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_user_saved_response = spotify.audiobooks.check_user_saved(
    ids="18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/audiobooks/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.audiobooks.get_catalog_info`<a id="spotifyaudiobooksget_catalog_info"></a>

Get Spotify catalog information for a single audiobook. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_catalog_info_response = spotify.audiobooks.get_catalog_info(
    id="7iHfbu1YPACw6oZPAFJtqe",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobookObject`](./spotify_python_sdk/pydantic/audiobook_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiobooks/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.audiobooks.get_chapters_by_id`<a id="spotifyaudiobooksget_chapters_by_id"></a>

Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_chapters_by_id_response = spotify.audiobooks.get_chapters_by_id(
    id="7iHfbu1YPACw6oZPAFJtqe",
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSimplifiedChapterObject`](./spotify_python_sdk/pydantic/paging_simplified_chapter_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiobooks/{id}/chapters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.audiobooks.get_several`<a id="spotifyaudiobooksget_several"></a>

Get Spotify catalog information for several audiobooks identified by their Spotify IDs. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_several_response = spotify.audiobooks.get_several(
    ids="18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksGetSeveralResponse`](./spotify_python_sdk/pydantic/audiobooks_get_several_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiobooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.audiobooks.list_saved`<a id="spotifyaudiobookslist_saved"></a>

Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_saved_response = spotify.audiobooks.list_saved(
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSimplifiedAudiobookObject`](./spotify_python_sdk/pydantic/paging_simplified_audiobook_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/audiobooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.audiobooks.remove_from_library`<a id="spotifyaudiobooksremove_from_library"></a>

Remove one or more audiobooks from the Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.audiobooks.remove_from_library(
    ids="18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/audiobooks` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.audiobooks.save_current_user_library`<a id="spotifyaudiobookssave_current_user_library"></a>

Save one or more audiobooks to the current Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.audiobooks.save_current_user_library(
    ids="18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/audiobooks` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.categories.get_category_playlists`<a id="spotifycategoriesget_category_playlists"></a>

Get a list of Spotify playlists tagged with a particular category.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_category_playlists_response = spotify.categories.get_category_playlists(
    category_id="dinner",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `str`<a id="category_id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingFeaturedPlaylistObject`](./spotify_python_sdk/pydantic/paging_featured_playlist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/browse/categories/{category_id}/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.categories.get_single`<a id="spotifycategoriesget_single"></a>

Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_response = spotify.categories.get_single(
    category_id="dinner",
    locale="sv_SE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `str`<a id="category_id-str"></a>

##### locale: `str`<a id="locale-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CategoryObject`](./spotify_python_sdk/pydantic/category_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/browse/categories/{category_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.categories.list_several`<a id="spotifycategorieslist_several"></a>

Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_several_response = spotify.categories.list_several(
    locale="sv_SE",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### locale: `str`<a id="locale-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CategoriesListSeveralResponse`](./spotify_python_sdk/pydantic/categories_list_several_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/browse/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.chapters.get_chapter_info`<a id="spotifychaptersget_chapter_info"></a>

Get Spotify catalog information for a single audiobook chapter. Chapters are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_chapter_info_response = spotify.chapters.get_chapter_info(
    id="0D5wENdkdwbqlrHoaJ9g29",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ChapterObject`](./spotify_python_sdk/pydantic/chapter_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chapters/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.chapters.get_chapters_by_id`<a id="spotifychaptersget_chapters_by_id"></a>

Get Spotify catalog information about an audiobook's chapters. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_chapters_by_id_response = spotify.chapters.get_chapters_by_id(
    id="7iHfbu1YPACw6oZPAFJtqe",
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSimplifiedChapterObject`](./spotify_python_sdk/pydantic/paging_simplified_chapter_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiobooks/{id}/chapters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.chapters.get_multiple_by_ids`<a id="spotifychaptersget_multiple_by_ids"></a>

Get Spotify catalog information for several audiobook chapters identified by their Spotify IDs. Chapters are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_multiple_by_ids_response = spotify.chapters.get_multiple_by_ids(
    ids="0IsXVP0JmcB2adSE338GkK,3ZXb8FKZGU0EHALYX6uCzU,0D5wENdkdwbqlrHoaJ9g29",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ChaptersGetMultipleByIdsResponse`](./spotify_python_sdk/pydantic/chapters_get_multiple_by_ids_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chapters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.episodes.check_saved_episodes`<a id="spotifyepisodescheck_saved_episodes"></a>

Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer)..


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_saved_episodes_response = spotify.episodes.check_saved_episodes(
    ids="77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/episodes/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.episodes.get_episodes_by_id`<a id="spotifyepisodesget_episodes_by_id"></a>

Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number of episodes returned.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_episodes_by_id_response = spotify.episodes.get_episodes_by_id(
    id="38bS44xjbVVZ3No3ByF1dJ",
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSimplifiedEpisodeObject`](./spotify_python_sdk/pydantic/paging_simplified_episode_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shows/{id}/episodes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.episodes.get_several`<a id="spotifyepisodesget_several"></a>

Get Spotify catalog information for several episodes based on their Spotify IDs.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_several_response = spotify.episodes.get_several(
    ids="77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EpisodesGetSeveralResponse`](./spotify_python_sdk/pydantic/episodes_get_several_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/episodes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.episodes.get_single_by_id`<a id="spotifyepisodesget_single_by_id"></a>

Get Spotify catalog information for a single episode identified by its
unique Spotify ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_by_id_response = spotify.episodes.get_single_by_id(
    id="512ojhOuo1ktJprKbVcKyQ",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EpisodeObject`](./spotify_python_sdk/pydantic/episode_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/episodes/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.episodes.get_user_saved_episodes`<a id="spotifyepisodesget_user_saved_episodes"></a>

Get a list of the episodes saved in the current Spotify user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_saved_episodes_response = spotify.episodes.get_user_saved_episodes(
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSavedEpisodeObject`](./spotify_python_sdk/pydantic/paging_saved_episode_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/episodes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.episodes.remove_from_library`<a id="spotifyepisodesremove_from_library"></a>

Remove one or more episodes from the current user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.episodes.remove_from_library(
    ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`EpisodesRemoveFromLibraryRequest`](./spotify_python_sdk/type/episodes_remove_from_library_request.py)<a id="requestbody-episodesremovefromlibraryrequestspotify_python_sdktypeepisodes_remove_from_library_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/episodes` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.episodes.save_current_user_library`<a id="spotifyepisodessave_current_user_library"></a>

Save one or more episodes to the current user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.episodes.save_current_user_library(
    ids="77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`EpisodesSaveCurrentUserLibraryRequest`](./spotify_python_sdk/type/episodes_save_current_user_library_request.py)<a id="requestbody-episodessavecurrentuserlibraryrequestspotify_python_sdktypeepisodes_save_current_user_library_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/episodes` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.genres.get_available_seeds`<a id="spotifygenresget_available_seeds"></a>

Retrieve a list of available genres seed parameter values for [recommendations](/documentation/web-api/reference/get-recommendations).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_available_seeds_response = spotify.genres.get_available_seeds()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GenresGetAvailableSeedsResponse`](./spotify_python_sdk/pydantic/genres_get_available_seeds_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recommendations/available-genre-seeds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.check_following_artists_users`<a id="spotifylibrarycheck_following_artists_users"></a>

Check to see if the current user is following one or more artists or other Spotify users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_following_artists_users_response = spotify.library.check_following_artists_users(
    type="artist",
    ids="2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.check_saved`<a id="spotifylibrarycheck_saved"></a>

Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_saved_response = spotify.library.check_saved(
    ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/albums/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.check_saved_0`<a id="spotifylibrarycheck_saved_0"></a>

Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_saved_0_response = spotify.library.check_saved_0(
    ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tracks/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.check_saved_episodes`<a id="spotifylibrarycheck_saved_episodes"></a>

Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer)..


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_saved_episodes_response = spotify.library.check_saved_episodes(
    ids="77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/episodes/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.check_saved_shows`<a id="spotifylibrarycheck_saved_shows"></a>

Check if one or more shows is already saved in the current Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_saved_shows_response = spotify.library.check_saved_shows(
    ids="5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/shows/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.check_user_saved`<a id="spotifylibrarycheck_user_saved"></a>

Check if one or more audiobooks are already saved in the current Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_user_saved_response = spotify.library.check_user_saved(
    ids="18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/audiobooks/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.create_playlist`<a id="spotifylibrarycreate_playlist"></a>

Create a playlist for a Spotify user. (The playlist will be empty until
you [add tracks](/documentation/web-api/reference/add-tracks-to-playlist).)
Each user is generally limited to a maximum of 11000 playlists.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_playlist_response = spotify.library.create_playlist(
    name="New Playlist",
    user_id="smedjan",
    description="New playlist description",
    public=False,
    collaborative=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name for the new playlist, for example `\\\"Your Coolest Playlist\\\"`. This name does not need to be unique; a user may have several playlists with the same name. 

##### user_id: `str`<a id="user_id-str"></a>

##### description: `str`<a id="description-str"></a>

value for playlist description as displayed in Spotify Clients and in the Web API. 

##### public: `bool`<a id="public-bool"></a>

Defaults to `true`. If `true` the playlist will be public, if `false` it will be private. To be able to create private playlists, the user must have granted the `playlist-modify-private` [scope](/documentation/web-api/concepts/scopes/#list-of-scopes) 

##### collaborative: `bool`<a id="collaborative-bool"></a>

Defaults to `false`. If `true` the playlist will be collaborative. _**Note**: to create a collaborative playlist you must also set `public` to `false`. To create collaborative playlists you must have granted `playlist-modify-private` and `playlist-modify-public` [scopes](/documentation/web-api/concepts/scopes/#list-of-scopes)._ 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlaylistsCreatePlaylistRequest`](./spotify_python_sdk/type/playlists_create_playlist_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PlaylistObject`](./spotify_python_sdk/pydantic/playlist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/playlists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.follow_artists_or_users`<a id="spotifylibraryfollow_artists_or_users"></a>

Add the current user as a follower of one or more artists or other Spotify users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.follow_artists_or_users(
    ids=[
        "string_example"
    ],
    type="artist",
    ids="2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`UsersFollowArtistsOrUsersRequest`](./spotify_python_sdk/type/users_follow_artists_or_users_request.py)<a id="requestbody-usersfollowartistsorusersrequestspotify_python_sdktypeusers_follow_artists_or_users_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.get_followed_artists`<a id="spotifylibraryget_followed_artists"></a>

Get the current user's followed artists.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_followed_artists_response = spotify.library.get_followed_artists(
    type="artist",
    after="0I2XqVXqHScXjHhk6AYYRe",
    limit=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetFollowedArtistsResponse`](./spotify_python_sdk/pydantic/users_get_followed_artists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.get_saved`<a id="spotifylibraryget_saved"></a>

Get a list of the albums saved in the current Spotify user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_saved_response = spotify.library.get_saved(
    limit=10,
    offset=5,
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSavedAlbumObject`](./spotify_python_sdk/pydantic/paging_saved_album_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/albums` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.get_top_items`<a id="spotifylibraryget_top_items"></a>

Get the current user's top artists or tracks based on calculated affinity.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_top_items_response = spotify.library.get_top_items(
    type="artists",
    time_range="medium_term",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### time_range: `str`<a id="time_range-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetTopItemsResponse`](./spotify_python_sdk/pydantic/users_get_top_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/top/{type}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.get_user_playlists`<a id="spotifylibraryget_user_playlists"></a>

Get a list of the playlists owned or followed by the current Spotify
user.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_playlists_response = spotify.library.get_user_playlists(
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingPlaylistObject`](./spotify_python_sdk/pydantic/paging_playlist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.get_user_saved`<a id="spotifylibraryget_user_saved"></a>

Get a list of the songs saved in the current Spotify user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_saved_response = spotify.library.get_user_saved(
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSavedTrackObject`](./spotify_python_sdk/pydantic/paging_saved_track_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.get_user_saved_episodes`<a id="spotifylibraryget_user_saved_episodes"></a>

Get a list of the episodes saved in the current Spotify user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_saved_episodes_response = spotify.library.get_user_saved_episodes(
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSavedEpisodeObject`](./spotify_python_sdk/pydantic/paging_saved_episode_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/episodes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.get_user_saved_shows`<a id="spotifylibraryget_user_saved_shows"></a>

Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the number of shows returned.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_saved_shows_response = spotify.library.get_user_saved_shows(
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSavedShowObject`](./spotify_python_sdk/pydantic/paging_saved_show_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/shows` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.list_saved`<a id="spotifylibrarylist_saved"></a>

Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_saved_response = spotify.library.list_saved(
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSimplifiedAudiobookObject`](./spotify_python_sdk/pydantic/paging_simplified_audiobook_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/audiobooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.remove_from_library`<a id="spotifylibraryremove_from_library"></a>

Remove one or more audiobooks from the Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.remove_from_library(
    ids="18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/audiobooks` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.remove_from_library_0`<a id="spotifylibraryremove_from_library_0"></a>

Remove one or more tracks from the current user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.remove_from_library_0(
    ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`TracksRemoveFromLibraryRequest`](./spotify_python_sdk/type/tracks_remove_from_library_request.py)<a id="requestbody-tracksremovefromlibraryrequestspotify_python_sdktypetracks_remove_from_library_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tracks` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.remove_from_library_1`<a id="spotifylibraryremove_from_library_1"></a>

Remove one or more episodes from the current user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.remove_from_library_1(
    ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`EpisodesRemoveFromLibraryRequest`](./spotify_python_sdk/type/episodes_remove_from_library_request.py)<a id="requestbody-episodesremovefromlibraryrequestspotify_python_sdktypeepisodes_remove_from_library_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/episodes` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.remove_saved`<a id="spotifylibraryremove_saved"></a>

Remove one or more albums from the current user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.remove_saved(
    ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`AlbumsRemoveSavedRequest`](./spotify_python_sdk/type/albums_remove_saved_request.py)<a id="requestbody-albumsremovesavedrequestspotify_python_sdktypealbums_remove_saved_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/albums` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.remove_user_library`<a id="spotifylibraryremove_user_library"></a>

Delete one or more shows from current Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.remove_user_library(
    ids="5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/shows` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.save_current_user_library`<a id="spotifylibrarysave_current_user_library"></a>

Save one or more audiobooks to the current Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.save_current_user_library(
    ids="18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/audiobooks` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.save_current_user_library_0`<a id="spotifylibrarysave_current_user_library_0"></a>

Save one or more albums to the current user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.save_current_user_library_0(
    ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`AlbumsSaveCurrentUserLibraryRequest`](./spotify_python_sdk/type/albums_save_current_user_library_request.py)<a id="requestbody-albumssavecurrentuserlibraryrequestspotify_python_sdktypealbums_save_current_user_library_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/albums` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.save_current_user_library_1`<a id="spotifylibrarysave_current_user_library_1"></a>

Save one or more episodes to the current user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.save_current_user_library_1(
    ids="77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`EpisodesSaveCurrentUserLibraryRequest`](./spotify_python_sdk/type/episodes_save_current_user_library_request.py)<a id="requestbody-episodessavecurrentuserlibraryrequestspotify_python_sdktypeepisodes_save_current_user_library_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/episodes` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.save_current_user_library_2`<a id="spotifylibrarysave_current_user_library_2"></a>

Save one or more shows to current Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.save_current_user_library_2(
    ids="5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/shows` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.save_for_current_user`<a id="spotifylibrarysave_for_current_user"></a>

Save one or more tracks to the current user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.save_for_current_user(
    ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`TracksSaveForCurrentUserRequest`](./spotify_python_sdk/type/tracks_save_for_current_user_request.py)<a id="requestbody-trackssaveforcurrentuserrequestspotify_python_sdktypetracks_save_for_current_user_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tracks` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.unfollow_artists_users`<a id="spotifylibraryunfollow_artists_users"></a>

Remove the current user as a follower of one or more artists or other Spotify users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.unfollow_artists_users(
    type="artist",
    ids="2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`UsersUnfollowArtistsUsersRequest`](./spotify_python_sdk/type/users_unfollow_artists_users_request.py)<a id="requestbody-usersunfollowartistsusersrequestspotify_python_sdktypeusers_unfollow_artists_users_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.library.update_details`<a id="spotifylibraryupdate_details"></a>

Change a playlist's name and public/private state. (The user must, of
course, own the playlist.)


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.library.update_details(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    description="Updated playlist description",
    name="Updated Playlist Name",
    public=False,
    collaborative=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### description: `str`<a id="description-str"></a>

Value for playlist description as displayed in Spotify Clients and in the Web API. 

##### name: `str`<a id="name-str"></a>

The new name for the playlist, for example `\\\"My New Playlist Title\\\"` 

##### public: `bool`<a id="public-bool"></a>

If `true` the playlist will be public, if `false` it will be private. 

##### collaborative: `bool`<a id="collaborative-bool"></a>

If `true`, the playlist will become collaborative and other users will be able to modify the playlist in their Spotify client. <br/> _**Note**: You can only set `collaborative` to `true` on non-public playlists._ 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlaylistsUpdateDetailsRequest`](./spotify_python_sdk/type/playlists_update_details_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.markets.list_available`<a id="spotifymarketslist_available"></a>

Get the list of markets where Spotify is available.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_available_response = spotify.markets.list_available()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MarketsListAvailableResponse`](./spotify_python_sdk/pydantic/markets_list_available_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/markets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.add_item_to_queue`<a id="spotifyplayeradd_item_to_queue"></a>

Add an item to the end of the user's current playback queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.player.add_item_to_queue(
    uri="spotify:track:4iV5W9uYEdYUVa79Axb7Rh",
    device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### uri: `str`<a id="uri-str"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/queue` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.get_available_devices`<a id="spotifyplayerget_available_devices"></a>

Get information about a user’s available Spotify Connect devices. Some device models are not supported and will not be listed in the API response.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_available_devices_response = spotify.player.get_available_devices()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PlayerGetAvailableDevicesResponse`](./spotify_python_sdk/pydantic/player_get_available_devices_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/devices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.get_current_playback_state`<a id="spotifyplayerget_current_playback_state"></a>

Get information about the user’s current playback state, including track or episode, progress, and active device.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_playback_state_response = spotify.player.get_current_playback_state(
    market="ES",
    additional_types="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### market: `str`<a id="market-str"></a>

##### additional_types: `str`<a id="additional_types-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CurrentlyPlayingContextObject`](./spotify_python_sdk/pydantic/currently_playing_context_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.get_currently_playing_track`<a id="spotifyplayerget_currently_playing_track"></a>

Get the object currently being played on the user's Spotify account.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_currently_playing_track_response = spotify.player.get_currently_playing_track(
    market="ES",
    additional_types="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### market: `str`<a id="market-str"></a>

##### additional_types: `str`<a id="additional_types-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CurrentlyPlayingContextObject`](./spotify_python_sdk/pydantic/currently_playing_context_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/currently-playing` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.get_recently_played_tracks`<a id="spotifyplayerget_recently_played_tracks"></a>

Get tracks from the current user's recently played tracks.
_**Note**: Currently doesn't support podcast episodes._


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recently_played_tracks_response = spotify.player.get_recently_played_tracks(
    limit=10,
    after=1484811043508,
    before=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### after: `int`<a id="after-int"></a>

##### before: `int`<a id="before-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CursorPagingPlayHistoryObject`](./spotify_python_sdk/pydantic/cursor_paging_play_history_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/recently-played` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.get_user_queue`<a id="spotifyplayerget_user_queue"></a>

Get the list of objects that make up the user's queue.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_queue_response = spotify.player.get_user_queue()
```

#### 🔄 Return<a id="🔄-return"></a>

[`QueueObject`](./spotify_python_sdk/pydantic/queue_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/queue` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.pause_playback`<a id="spotifyplayerpause_playback"></a>

Pause playback on the user's account. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.player.pause_playback(
    device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/pause` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.seek_to_position`<a id="spotifyplayerseek_to_position"></a>

Seeks to the given position in the user’s currently playing track. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.player.seek_to_position(
    position_ms=25000,
    device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### position_ms: `int`<a id="position_ms-int"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/seek` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.set_playback_volume`<a id="spotifyplayerset_playback_volume"></a>

Set the volume for the user’s current playback device. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.player.set_playback_volume(
    volume_percent=50,
    device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### volume_percent: `int`<a id="volume_percent-int"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/volume` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.set_repeat_mode`<a id="spotifyplayerset_repeat_mode"></a>

Set the repeat mode for the user's playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.player.set_repeat_mode(
    state="context",
    device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### state: `str`<a id="state-str"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/repeat` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.skip_to_next_track`<a id="spotifyplayerskip_to_next_track"></a>

Skips to next track in the user’s queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.player.skip_to_next_track(
    device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/next` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.skip_to_previous_track`<a id="spotifyplayerskip_to_previous_track"></a>

Skips to previous track in the user’s queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.player.skip_to_previous_track(
    device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/previous` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.start_playback`<a id="spotifyplayerstart_playback"></a>

Start a new context or resume current playback on the user's active device. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.player.start_playback(
    context_uri={},
    uris=[
        "string_example"
    ],
    offset={},
    position_ms={},
    device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### context_uri: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="context_uri-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Optional. Spotify URI of the context to play. Valid contexts are albums, artists & playlists. `{context_uri:\\\"spotify:album:1Je1IMUlBXcx1Fz0WE7oPT\\\"}` 

##### uris: [`PlayerStartPlaybackRequestUris`](./spotify_python_sdk/type/player_start_playback_request_uris.py)<a id="uris-playerstartplaybackrequesturisspotify_python_sdktypeplayer_start_playback_request_urispy"></a>

##### offset: [`PlayerStartPlaybackRequestOffset`](./spotify_python_sdk/type/player_start_playback_request_offset.py)<a id="offset-playerstartplaybackrequestoffsetspotify_python_sdktypeplayer_start_playback_request_offsetpy"></a>

##### position_ms: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="position_ms-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

integer

##### device_id: `str`<a id="device_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlayerStartPlaybackRequest`](./spotify_python_sdk/type/player_start_playback_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/play` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.toggle_playback_shuffle`<a id="spotifyplayertoggle_playback_shuffle"></a>

Toggle shuffle on or off for user’s playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.player.toggle_playback_shuffle(
    state=True,
    device_id="0d1841b0976bae2a3a310dd74c0f3df354899bc8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### state: `bool`<a id="state-bool"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player/shuffle` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.player.transfer_playback_to_new_device`<a id="spotifyplayertransfer_playback_to_new_device"></a>

Transfer playback to a new device and optionally begin playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.player.transfer_playback_to_new_device(
    device_ids=[
        "string_example"
    ],
    play={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_ids: [`PlayerTransferPlaybackToNewDeviceRequestDeviceIds`](./spotify_python_sdk/type/player_transfer_playback_to_new_device_request_device_ids.py)<a id="device_ids-playertransferplaybacktonewdevicerequestdeviceidsspotify_python_sdktypeplayer_transfer_playback_to_new_device_request_device_idspy"></a>

##### play: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="play-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

**true**: ensure playback happens on new device.<br/>**false** or not provided: keep the current playback state. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlayerTransferPlaybackToNewDeviceRequest`](./spotify_python_sdk/type/player_transfer_playback_to_new_device_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/player` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.add_items`<a id="spotifyplaylistsadd_items"></a>

Add one or more items to a user's playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_items_response = spotify.playlists.add_items(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    uris=[
        "string_example"
    ],
    position=1,
    position=0,
    uris="spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### position: `int`<a id="position-int"></a>

##### uris: `str`<a id="uris-str"></a>

##### requestBody: [`PlaylistsAddItemsRequest`](./spotify_python_sdk/type/playlists_add_items_request.py)<a id="requestbody-playlistsadditemsrequestspotify_python_sdktypeplaylists_add_items_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PlaylistsRemoveItemsResponse`](./spotify_python_sdk/pydantic/playlists_remove_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/tracks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.check_if_follows_playlist`<a id="spotifyplaylistscheck_if_follows_playlist"></a>

Check to see if one or more Spotify users are following a specified playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_if_follows_playlist_response = spotify.playlists.check_if_follows_playlist(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    ids="jmperezperez,thelinmichael,wizzler",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/followers/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.create_playlist`<a id="spotifyplaylistscreate_playlist"></a>

Create a playlist for a Spotify user. (The playlist will be empty until
you [add tracks](/documentation/web-api/reference/add-tracks-to-playlist).)
Each user is generally limited to a maximum of 11000 playlists.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_playlist_response = spotify.playlists.create_playlist(
    name="New Playlist",
    user_id="smedjan",
    description="New playlist description",
    public=False,
    collaborative=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name for the new playlist, for example `\\\"Your Coolest Playlist\\\"`. This name does not need to be unique; a user may have several playlists with the same name. 

##### user_id: `str`<a id="user_id-str"></a>

##### description: `str`<a id="description-str"></a>

value for playlist description as displayed in Spotify Clients and in the Web API. 

##### public: `bool`<a id="public-bool"></a>

Defaults to `true`. If `true` the playlist will be public, if `false` it will be private. To be able to create private playlists, the user must have granted the `playlist-modify-private` [scope](/documentation/web-api/concepts/scopes/#list-of-scopes) 

##### collaborative: `bool`<a id="collaborative-bool"></a>

Defaults to `false`. If `true` the playlist will be collaborative. _**Note**: to create a collaborative playlist you must also set `public` to `false`. To create collaborative playlists you must have granted `playlist-modify-private` and `playlist-modify-public` [scopes](/documentation/web-api/concepts/scopes/#list-of-scopes)._ 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlaylistsCreatePlaylistRequest`](./spotify_python_sdk/type/playlists_create_playlist_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PlaylistObject`](./spotify_python_sdk/pydantic/playlist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/playlists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.follow_playlist`<a id="spotifyplaylistsfollow_playlist"></a>

Add the current user as a follower of a playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.playlists.follow_playlist(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    public=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### public: `bool`<a id="public-bool"></a>

Defaults to `true`. If `true` the playlist will be included in user's public playlists, if `false` it will remain private. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersFollowPlaylistRequest`](./spotify_python_sdk/type/users_follow_playlist_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/followers` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.get_category_playlists`<a id="spotifyplaylistsget_category_playlists"></a>

Get a list of Spotify playlists tagged with a particular category.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_category_playlists_response = spotify.playlists.get_category_playlists(
    category_id="dinner",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `str`<a id="category_id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingFeaturedPlaylistObject`](./spotify_python_sdk/pydantic/paging_featured_playlist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/browse/categories/{category_id}/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.get_cover_image`<a id="spotifyplaylistsget_cover_image"></a>

Get the current image associated with a specific playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cover_image_response = spotify.playlists.get_cover_image(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PlaylistsGetCoverImageResponse`](./spotify_python_sdk/pydantic/playlists_get_cover_image_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/images` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.get_featured`<a id="spotifyplaylistsget_featured"></a>

Get a list of Spotify featured playlists (shown, for example, on a Spotify player's 'Browse' tab).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_featured_response = spotify.playlists.get_featured(
    locale="sv_SE",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### locale: `str`<a id="locale-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingFeaturedPlaylistObject`](./spotify_python_sdk/pydantic/paging_featured_playlist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/browse/featured-playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.get_playlist_by_id`<a id="spotifyplaylistsget_playlist_by_id"></a>

Get a playlist owned by a Spotify user.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_playlist_by_id_response = spotify.playlists.get_playlist_by_id(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    market="ES",
    fields="items(added_by.id,track(name,href,album(name,href)))",
    additional_types="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### market: `str`<a id="market-str"></a>

##### fields: `str`<a id="fields-str"></a>

##### additional_types: `str`<a id="additional_types-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PlaylistObject`](./spotify_python_sdk/pydantic/playlist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.get_playlist_items`<a id="spotifyplaylistsget_playlist_items"></a>

Get full details of the items of a playlist owned by a Spotify user.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_playlist_items_response = spotify.playlists.get_playlist_items(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    market="ES",
    fields="items(added_by.id,track(name,href,album(name,href)))",
    limit=10,
    offset=5,
    additional_types="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### market: `str`<a id="market-str"></a>

##### fields: `str`<a id="fields-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

##### additional_types: `str`<a id="additional_types-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingPlaylistTrackObject`](./spotify_python_sdk/pydantic/paging_playlist_track_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.get_user_playlists`<a id="spotifyplaylistsget_user_playlists"></a>

Get a list of the playlists owned or followed by the current Spotify
user.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_playlists_response = spotify.playlists.get_user_playlists(
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingPlaylistObject`](./spotify_python_sdk/pydantic/paging_playlist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.get_user_playlists_0`<a id="spotifyplaylistsget_user_playlists_0"></a>

Get a list of the playlists owned or followed by a Spotify user.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_playlists_0_response = spotify.playlists.get_user_playlists_0(
    user_id="smedjan",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingPlaylistObject`](./spotify_python_sdk/pydantic/paging_playlist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.remove_items`<a id="spotifyplaylistsremove_items"></a>

Remove one or more items from a user's playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_items_response = spotify.playlists.remove_items(
    tracks=[
        {
        }
    ],
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    snapshot_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tracks: [`PlaylistsRemoveItemsRequestTracks`](./spotify_python_sdk/type/playlists_remove_items_request_tracks.py)<a id="tracks-playlistsremoveitemsrequesttracksspotify_python_sdktypeplaylists_remove_items_request_trackspy"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### snapshot_id: `str`<a id="snapshot_id-str"></a>

The playlist's snapshot ID against which you want to make the changes. The API will validate that the specified items exist and in the specified positions and make the changes, even if more recent changes have been made to the playlist. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlaylistsRemoveItemsRequest`](./spotify_python_sdk/type/playlists_remove_items_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PlaylistsRemoveItemsResponse`](./spotify_python_sdk/pydantic/playlists_remove_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/tracks` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.replace_cover_image`<a id="spotifyplaylistsreplace_cover_image"></a>

Replace the image used to represent a specific playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.playlists.replace_cover_image(
    body="/9j/2wCEABoZGSccJz4lJT5CLy8vQkc9Ozs9R0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0cBHCcnMyYzPSYmPUc9Mj1HR0dEREdHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR//dAAQAAf/uAA5BZG9iZQBkwAAAAAH/wAARCAABAAEDACIAAREBAhEB/8QASwABAQAAAAAAAAAAAAAAAAAAAAYBAQAAAAAAAAAAAAAAAAAAAAAQAQAAAAAAAAAAAAAAAAAAAAARAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwAAARECEQA/AJgAH//Z",
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### requestBody: `str`<a id="requestbody-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/images` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.unfollow_playlist`<a id="spotifyplaylistsunfollow_playlist"></a>

Remove the current user as a follower of a playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.playlists.unfollow_playlist(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/followers` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.update_details`<a id="spotifyplaylistsupdate_details"></a>

Change a playlist's name and public/private state. (The user must, of
course, own the playlist.)


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.playlists.update_details(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    description="Updated playlist description",
    name="Updated Playlist Name",
    public=False,
    collaborative=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### description: `str`<a id="description-str"></a>

Value for playlist description as displayed in Spotify Clients and in the Web API. 

##### name: `str`<a id="name-str"></a>

The new name for the playlist, for example `\\\"My New Playlist Title\\\"` 

##### public: `bool`<a id="public-bool"></a>

If `true` the playlist will be public, if `false` it will be private. 

##### collaborative: `bool`<a id="collaborative-bool"></a>

If `true`, the playlist will become collaborative and other users will be able to modify the playlist in their Spotify client. <br/> _**Note**: You can only set `collaborative` to `true` on non-public playlists._ 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlaylistsUpdateDetailsRequest`](./spotify_python_sdk/type/playlists_update_details_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.playlists.update_playlist_items`<a id="spotifyplaylistsupdate_playlist_items"></a>

Either reorder or replace items in a playlist depending on the request's parameters.
To reorder items, include `range_start`, `insert_before`, `range_length` and `snapshot_id` in the request's body.
To replace items, include `uris` as either a query parameter or in the request's body.
Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist.
<br/>
**Note**: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters.
These operations can't be applied together in a single request.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_playlist_items_response = spotify.playlists.update_playlist_items(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    uris=[
        "string_example"
    ],
    range_start=1,
    insert_before=3,
    range_length=2,
    snapshot_id="string_example",
    uris="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### uris: `str`<a id="uris-str"></a>

##### requestBody: [`PlaylistsUpdatePlaylistItemsRequest`](./spotify_python_sdk/type/playlists_update_playlist_items_request.py)<a id="requestbody-playlistsupdateplaylistitemsrequestspotify_python_sdktypeplaylists_update_playlist_items_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PlaylistsRemoveItemsResponse`](./spotify_python_sdk/pydantic/playlists_remove_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/tracks` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.search.spotify_catalog_info`<a id="spotifysearchspotify_catalog_info"></a>

Get Spotify catalog information about albums, artists, playlists, tracks, shows, episodes or audiobooks
that match a keyword string. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify_catalog_info_response = spotify.search.spotify_catalog_info(
    q="remaster%20track:Doxy%20artist:Miles%20Davis",
    type=[
        "album"
    ],
    market="ES",
    limit=10,
    offset=5,
    include_external="audio",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

##### type: List[`str`]<a id="type-liststr"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

##### include_external: `str`<a id="include_external-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SearchSpotifyCatalogInfoResponse`](./spotify_python_sdk/pydantic/search_spotify_catalog_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.shows.check_saved_shows`<a id="spotifyshowscheck_saved_shows"></a>

Check if one or more shows is already saved in the current Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_saved_shows_response = spotify.shows.check_saved_shows(
    ids="5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/shows/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.shows.get_episodes_by_id`<a id="spotifyshowsget_episodes_by_id"></a>

Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number of episodes returned.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_episodes_by_id_response = spotify.shows.get_episodes_by_id(
    id="38bS44xjbVVZ3No3ByF1dJ",
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSimplifiedEpisodeObject`](./spotify_python_sdk/pydantic/paging_simplified_episode_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shows/{id}/episodes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.shows.get_information`<a id="spotifyshowsget_information"></a>

Get Spotify catalog information for a single show identified by its
unique Spotify ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = spotify.shows.get_information(
    id="38bS44xjbVVZ3No3ByF1dJ",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ShowObject`](./spotify_python_sdk/pydantic/show_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shows/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.shows.get_multiple_shows_info`<a id="spotifyshowsget_multiple_shows_info"></a>

Get Spotify catalog information for several shows based on their Spotify IDs.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_multiple_shows_info_response = spotify.shows.get_multiple_shows_info(
    ids="5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ShowsGetMultipleShowsInfoResponse`](./spotify_python_sdk/pydantic/shows_get_multiple_shows_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shows` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.shows.get_user_saved_shows`<a id="spotifyshowsget_user_saved_shows"></a>

Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the number of shows returned.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_saved_shows_response = spotify.shows.get_user_saved_shows(
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSavedShowObject`](./spotify_python_sdk/pydantic/paging_saved_show_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/shows` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.shows.remove_user_library`<a id="spotifyshowsremove_user_library"></a>

Delete one or more shows from current Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.shows.remove_user_library(
    ids="5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/shows` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.shows.save_current_user_library`<a id="spotifyshowssave_current_user_library"></a>

Save one or more shows to current Spotify user's library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.shows.save_current_user_library(
    ids="5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/shows` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.add_items`<a id="spotifytracksadd_items"></a>

Add one or more items to a user's playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_items_response = spotify.tracks.add_items(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    uris=[
        "string_example"
    ],
    position=1,
    position=0,
    uris="spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### position: `int`<a id="position-int"></a>

##### uris: `str`<a id="uris-str"></a>

##### requestBody: [`PlaylistsAddItemsRequest`](./spotify_python_sdk/type/playlists_add_items_request.py)<a id="requestbody-playlistsadditemsrequestspotify_python_sdktypeplaylists_add_items_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PlaylistsRemoveItemsResponse`](./spotify_python_sdk/pydantic/playlists_remove_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/tracks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.check_saved`<a id="spotifytrackscheck_saved"></a>

Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_saved_response = spotify.tracks.check_saved(
    ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tracks/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_audio_analysis`<a id="spotifytracksget_audio_analysis"></a>

Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s structure and musical content, including rhythm, pitch, and timbre.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_audio_analysis_response = spotify.tracks.get_audio_analysis(
    id="11dFghVXANMlKmJXsNCbNl",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudioAnalysisObject`](./spotify_python_sdk/pydantic/audio_analysis_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audio-analysis/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_audio_features_by_id`<a id="spotifytracksget_audio_features_by_id"></a>

Get audio feature information for a single track identified by its unique
Spotify ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_audio_features_by_id_response = spotify.tracks.get_audio_features_by_id(
    id="11dFghVXANMlKmJXsNCbNl",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudioFeaturesObject`](./spotify_python_sdk/pydantic/audio_features_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audio-features/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_by_spotify_id`<a id="spotifytracksget_by_spotify_id"></a>

Get Spotify catalog information for a single track identified by its
unique Spotify ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_spotify_id_response = spotify.tracks.get_by_spotify_id(
    id="11dFghVXANMlKmJXsNCbNl",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TrackObject`](./spotify_python_sdk/pydantic/track_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_multiple_audio_features`<a id="spotifytracksget_multiple_audio_features"></a>

Get audio features for multiple tracks based on their Spotify IDs.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_multiple_audio_features_response = spotify.tracks.get_multiple_audio_features(
    ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TracksGetMultipleAudioFeaturesResponse`](./spotify_python_sdk/pydantic/tracks_get_multiple_audio_features_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audio-features` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_multiple_by_ids`<a id="spotifytracksget_multiple_by_ids"></a>

Get Spotify catalog information for multiple tracks based on their Spotify IDs.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_multiple_by_ids_response = spotify.tracks.get_multiple_by_ids(
    ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ArtistsGetTopTracksResponse`](./spotify_python_sdk/pydantic/artists_get_top_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_playlist_items`<a id="spotifytracksget_playlist_items"></a>

Get full details of the items of a playlist owned by a Spotify user.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_playlist_items_response = spotify.tracks.get_playlist_items(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    market="ES",
    fields="items(added_by.id,track(name,href,album(name,href)))",
    limit=10,
    offset=5,
    additional_types="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### market: `str`<a id="market-str"></a>

##### fields: `str`<a id="fields-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

##### additional_types: `str`<a id="additional_types-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingPlaylistTrackObject`](./spotify_python_sdk/pydantic/paging_playlist_track_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_recommendations`<a id="spotifytracksget_recommendations"></a>

Recommendations are generated based on the available information for a given seed entity and matched against similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will be returned together with pool size details.

For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recommendations_response = spotify.tracks.get_recommendations(
    seed_artists="4NHQUGzhtTLFvgF5SZesLK",
    seed_genres="classical,country",
    seed_tracks="0c6xIDDpzE81m2q797ordA",
    limit=10,
    market="ES",
    min_acousticness=0,
    max_acousticness=0,
    target_acousticness=0,
    min_danceability=0,
    max_danceability=0,
    target_danceability=0,
    min_duration_ms=1,
    max_duration_ms=1,
    target_duration_ms=1,
    min_energy=0,
    max_energy=0,
    target_energy=0,
    min_instrumentalness=0,
    max_instrumentalness=0,
    target_instrumentalness=0,
    min_key=0,
    max_key=0,
    target_key=0,
    min_liveness=0,
    max_liveness=0,
    target_liveness=0,
    min_loudness=3.14,
    max_loudness=3.14,
    target_loudness=3.14,
    min_mode=0,
    max_mode=0,
    target_mode=0,
    min_popularity=0,
    max_popularity=0,
    target_popularity=0,
    min_speechiness=0,
    max_speechiness=0,
    target_speechiness=0,
    min_tempo=3.14,
    max_tempo=3.14,
    target_tempo=3.14,
    min_time_signature=1,
    max_time_signature=1,
    target_time_signature=1,
    min_valence=0,
    max_valence=0,
    target_valence=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### seed_artists: `str`<a id="seed_artists-str"></a>

##### seed_genres: `str`<a id="seed_genres-str"></a>

##### seed_tracks: `str`<a id="seed_tracks-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### market: `str`<a id="market-str"></a>

##### min_acousticness: `Union[int, float]`<a id="min_acousticness-unionint-float"></a>

##### max_acousticness: `Union[int, float]`<a id="max_acousticness-unionint-float"></a>

##### target_acousticness: `Union[int, float]`<a id="target_acousticness-unionint-float"></a>

##### min_danceability: `Union[int, float]`<a id="min_danceability-unionint-float"></a>

##### max_danceability: `Union[int, float]`<a id="max_danceability-unionint-float"></a>

##### target_danceability: `Union[int, float]`<a id="target_danceability-unionint-float"></a>

##### min_duration_ms: `int`<a id="min_duration_ms-int"></a>

##### max_duration_ms: `int`<a id="max_duration_ms-int"></a>

##### target_duration_ms: `int`<a id="target_duration_ms-int"></a>

##### min_energy: `Union[int, float]`<a id="min_energy-unionint-float"></a>

##### max_energy: `Union[int, float]`<a id="max_energy-unionint-float"></a>

##### target_energy: `Union[int, float]`<a id="target_energy-unionint-float"></a>

##### min_instrumentalness: `Union[int, float]`<a id="min_instrumentalness-unionint-float"></a>

##### max_instrumentalness: `Union[int, float]`<a id="max_instrumentalness-unionint-float"></a>

##### target_instrumentalness: `Union[int, float]`<a id="target_instrumentalness-unionint-float"></a>

##### min_key: `int`<a id="min_key-int"></a>

##### max_key: `int`<a id="max_key-int"></a>

##### target_key: `int`<a id="target_key-int"></a>

##### min_liveness: `Union[int, float]`<a id="min_liveness-unionint-float"></a>

##### max_liveness: `Union[int, float]`<a id="max_liveness-unionint-float"></a>

##### target_liveness: `Union[int, float]`<a id="target_liveness-unionint-float"></a>

##### min_loudness: `Union[int, float]`<a id="min_loudness-unionint-float"></a>

##### max_loudness: `Union[int, float]`<a id="max_loudness-unionint-float"></a>

##### target_loudness: `Union[int, float]`<a id="target_loudness-unionint-float"></a>

##### min_mode: `int`<a id="min_mode-int"></a>

##### max_mode: `int`<a id="max_mode-int"></a>

##### target_mode: `int`<a id="target_mode-int"></a>

##### min_popularity: `int`<a id="min_popularity-int"></a>

##### max_popularity: `int`<a id="max_popularity-int"></a>

##### target_popularity: `int`<a id="target_popularity-int"></a>

##### min_speechiness: `Union[int, float]`<a id="min_speechiness-unionint-float"></a>

##### max_speechiness: `Union[int, float]`<a id="max_speechiness-unionint-float"></a>

##### target_speechiness: `Union[int, float]`<a id="target_speechiness-unionint-float"></a>

##### min_tempo: `Union[int, float]`<a id="min_tempo-unionint-float"></a>

##### max_tempo: `Union[int, float]`<a id="max_tempo-unionint-float"></a>

##### target_tempo: `Union[int, float]`<a id="target_tempo-unionint-float"></a>

##### min_time_signature: `int`<a id="min_time_signature-int"></a>

##### max_time_signature: `int`<a id="max_time_signature-int"></a>

##### target_time_signature: `int`<a id="target_time_signature-int"></a>

##### min_valence: `Union[int, float]`<a id="min_valence-unionint-float"></a>

##### max_valence: `Union[int, float]`<a id="max_valence-unionint-float"></a>

##### target_valence: `Union[int, float]`<a id="target_valence-unionint-float"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RecommendationsObject`](./spotify_python_sdk/pydantic/recommendations_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recommendations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_top_items`<a id="spotifytracksget_top_items"></a>

Get the current user's top artists or tracks based on calculated affinity.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_top_items_response = spotify.tracks.get_top_items(
    type="artists",
    time_range="medium_term",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### time_range: `str`<a id="time_range-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetTopItemsResponse`](./spotify_python_sdk/pydantic/users_get_top_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/top/{type}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_top_tracks`<a id="spotifytracksget_top_tracks"></a>

Get Spotify catalog information about an artist's top tracks by country.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_top_tracks_response = spotify.tracks.get_top_tracks(
    id="0TnOYISbd1XYRBk9myaseg",
    market="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ArtistsGetTopTracksResponse`](./spotify_python_sdk/pydantic/artists_get_top_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/artists/{id}/top-tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_tracks_by_id`<a id="spotifytracksget_tracks_by_id"></a>

Get Spotify catalog information about an album’s tracks.
Optional parameters can be used to limit the number of tracks returned.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tracks_by_id_response = spotify.tracks.get_tracks_by_id(
    id="4aawyAB9vmqN3uQ7FjRGTy",
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSimplifiedTrackObject`](./spotify_python_sdk/pydantic/paging_simplified_track_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/albums/{id}/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.get_user_saved`<a id="spotifytracksget_user_saved"></a>

Get a list of the songs saved in the current Spotify user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_saved_response = spotify.tracks.get_user_saved(
    market="ES",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### market: `str`<a id="market-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingSavedTrackObject`](./spotify_python_sdk/pydantic/paging_saved_track_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.remove_from_library`<a id="spotifytracksremove_from_library"></a>

Remove one or more tracks from the current user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.tracks.remove_from_library(
    ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`TracksRemoveFromLibraryRequest`](./spotify_python_sdk/type/tracks_remove_from_library_request.py)<a id="requestbody-tracksremovefromlibraryrequestspotify_python_sdktypetracks_remove_from_library_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tracks` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.remove_items`<a id="spotifytracksremove_items"></a>

Remove one or more items from a user's playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_items_response = spotify.tracks.remove_items(
    tracks=[
        {
        }
    ],
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    snapshot_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tracks: [`PlaylistsRemoveItemsRequestTracks`](./spotify_python_sdk/type/playlists_remove_items_request_tracks.py)<a id="tracks-playlistsremoveitemsrequesttracksspotify_python_sdktypeplaylists_remove_items_request_trackspy"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### snapshot_id: `str`<a id="snapshot_id-str"></a>

The playlist's snapshot ID against which you want to make the changes. The API will validate that the specified items exist and in the specified positions and make the changes, even if more recent changes have been made to the playlist. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlaylistsRemoveItemsRequest`](./spotify_python_sdk/type/playlists_remove_items_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PlaylistsRemoveItemsResponse`](./spotify_python_sdk/pydantic/playlists_remove_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/tracks` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.save_for_current_user`<a id="spotifytrackssave_for_current_user"></a>

Save one or more tracks to the current user's 'Your Music' library.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.tracks.save_for_current_user(
    ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`TracksSaveForCurrentUserRequest`](./spotify_python_sdk/type/tracks_save_for_current_user_request.py)<a id="requestbody-trackssaveforcurrentuserrequestspotify_python_sdktypetracks_save_for_current_user_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tracks` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.tracks.update_playlist_items`<a id="spotifytracksupdate_playlist_items"></a>

Either reorder or replace items in a playlist depending on the request's parameters.
To reorder items, include `range_start`, `insert_before`, `range_length` and `snapshot_id` in the request's body.
To replace items, include `uris` as either a query parameter or in the request's body.
Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist.
<br/>
**Note**: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters.
These operations can't be applied together in a single request.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_playlist_items_response = spotify.tracks.update_playlist_items(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    uris=[
        "string_example"
    ],
    range_start=1,
    insert_before=3,
    range_length=2,
    snapshot_id="string_example",
    uris="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### uris: `str`<a id="uris-str"></a>

##### requestBody: [`PlaylistsUpdatePlaylistItemsRequest`](./spotify_python_sdk/type/playlists_update_playlist_items_request.py)<a id="requestbody-playlistsupdateplaylistitemsrequestspotify_python_sdktypeplaylists_update_playlist_items_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PlaylistsRemoveItemsResponse`](./spotify_python_sdk/pydantic/playlists_remove_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/tracks` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.check_following_artists_users`<a id="spotifyuserscheck_following_artists_users"></a>

Check to see if the current user is following one or more artists or other Spotify users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_following_artists_users_response = spotify.users.check_following_artists_users(
    type="artist",
    ids="2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.check_if_follows_playlist`<a id="spotifyuserscheck_if_follows_playlist"></a>

Check to see if one or more Spotify users are following a specified playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_if_follows_playlist_response = spotify.users.check_if_follows_playlist(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    ids="jmperezperez,thelinmichael,wizzler",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### ids: `str`<a id="ids-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AudiobooksCheckUserSavedResponse`](./spotify_python_sdk/pydantic/audiobooks_check_user_saved_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/followers/contains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.follow_artists_or_users`<a id="spotifyusersfollow_artists_or_users"></a>

Add the current user as a follower of one or more artists or other Spotify users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.users.follow_artists_or_users(
    ids=[
        "string_example"
    ],
    type="artist",
    ids="2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`UsersFollowArtistsOrUsersRequest`](./spotify_python_sdk/type/users_follow_artists_or_users_request.py)<a id="requestbody-usersfollowartistsorusersrequestspotify_python_sdktypeusers_follow_artists_or_users_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.follow_playlist`<a id="spotifyusersfollow_playlist"></a>

Add the current user as a follower of a playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.users.follow_playlist(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
    public=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

##### public: `bool`<a id="public-bool"></a>

Defaults to `true`. If `true` the playlist will be included in user's public playlists, if `false` it will remain private. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersFollowPlaylistRequest`](./spotify_python_sdk/type/users_follow_playlist_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/followers` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.get_current_user_profile`<a id="spotifyusersget_current_user_profile"></a>

Get detailed profile information about the current user (including the
current user's username).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_user_profile_response = spotify.users.get_current_user_profile()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PrivateUserObject`](./spotify_python_sdk/pydantic/private_user_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.get_followed_artists`<a id="spotifyusersget_followed_artists"></a>

Get the current user's followed artists.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_followed_artists_response = spotify.users.get_followed_artists(
    type="artist",
    after="0I2XqVXqHScXjHhk6AYYRe",
    limit=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetFollowedArtistsResponse`](./spotify_python_sdk/pydantic/users_get_followed_artists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.get_top_items`<a id="spotifyusersget_top_items"></a>

Get the current user's top artists or tracks based on calculated affinity.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_top_items_response = spotify.users.get_top_items(
    type="artists",
    time_range="medium_term",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### time_range: `str`<a id="time_range-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetTopItemsResponse`](./spotify_python_sdk/pydantic/users_get_top_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/top/{type}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.get_user_playlists`<a id="spotifyusersget_user_playlists"></a>

Get a list of the playlists owned or followed by a Spotify user.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_playlists_response = spotify.users.get_user_playlists(
    user_id="smedjan",
    limit=10,
    offset=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagingPlaylistObject`](./spotify_python_sdk/pydantic/paging_playlist_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.get_user_profile`<a id="spotifyusersget_user_profile"></a>

Get public profile information about a Spotify user.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_profile_response = spotify.users.get_user_profile(
    user_id="smedjan",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicUserObject`](./spotify_python_sdk/pydantic/public_user_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.unfollow_artists_users`<a id="spotifyusersunfollow_artists_users"></a>

Remove the current user as a follower of one or more artists or other Spotify users.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.users.unfollow_artists_users(
    type="artist",
    ids="2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6",
    ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### ids: `str`<a id="ids-str"></a>

##### requestBody: [`UsersUnfollowArtistsUsersRequest`](./spotify_python_sdk/type/users_unfollow_artists_users_request.py)<a id="requestbody-usersunfollowartistsusersrequestspotify_python_sdktypeusers_unfollow_artists_users_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/following` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `spotify.users.unfollow_playlist`<a id="spotifyusersunfollow_playlist"></a>

Remove the current user as a follower of a playlist.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
spotify.users.unfollow_playlist(
    playlist_id="3cEYpjA9oz9GiPac4AsH4n",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `str`<a id="playlist_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/followers` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
