import requests
from django.conf import settings


GENIUS_API_KEY = getattr(settings, 'GENIUS_API_KEY', None)
def get_artist_albums(artist_id):

    url = "https://genius-song-lyrics1.p.rapidapi.com/artist/albums/"

    querystring = {"id": artist_id, "sort": "title", "per_page": "20", "page": "1"}

    headers = {
        "x-rapidapi-key": GENIUS_API_KEY,
        "x-rapidapi-host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()

    albums = response['albums']
    for x in albums:
        album_id = x['id']
        print(type(album_id))
        # albums(album_id)

def album_details(album_id):
    print(album_id)
    url = "https://genius-song-lyrics1.p.rapidapi.com/album/details/"

    querystring = {"id": album_id}

    headers = {
        "x-rapidapi-key": GENIUS_API_KEY,
        "x-rapidapi-host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response)

def artist_songs(artist_id,page):
    url = "https://genius-song-lyrics1.p.rapidapi.com/artist/songs/"

    querystring = {"id": artist_id, "sort": "title", "per_page": "50", "page": page}

    headers = {
        "x-rapidapi-key": GENIUS_API_KEY,
        "x-rapidapi-host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response =  requests.get(url, headers=headers, params=querystring)
    print(response.status_code)



def collect_songs(songs):
    filtered_songs = []
    for x in songs:
        filtered_songs.append(x['id'])

    return filtered_songs


def recursive_collection(artist_id,page):
    if not page:
        return

    info = artist_songs(artist_id, page)
    print(info)
    # filtered_songs = collect_songs(info['songs'])
    # return filtered_songs, recursive_collection(artist_id,info['next_page'])


