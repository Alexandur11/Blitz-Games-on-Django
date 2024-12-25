from bs4 import BeautifulSoup


def parse_lyrics_response(response_data):
    lyrics_data = response_data['lyrics']
    lyrics = lyrics_data['lyrics']
    body = lyrics['body']
    track_data = lyrics_data['tracking_data']

    html_content = body['html']
    song_title = track_data['title']
    artist = track_data['primary_artist']

    return {'artist':artist,'title':song_title,'html_content':html_content}

def parse_song_lyrics(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    parsed_data = []

    song_verses = []

    for anchor in soup.find_all('a'):
        data_classification = anchor.get('data-classification', 'N/A')
        data_id = anchor.get('data-id', 'N/A')
        lyrics = anchor.text.strip()

        parsed_data.append({
            "data_id": data_id,
            "data_classification": data_classification,
            "lyrics": lyrics
        })

    for item in parsed_data:
        song_verses.append({item['lyrics']})
        print(f"\nLyrics: {item['lyrics']}\n")

    return song_verses