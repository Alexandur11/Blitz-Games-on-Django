import pytest
from .utilities.parsing_utilities import *
from .test_data import data
from .services.music_service import MusicService

MA = MusicService()
def test_parse_lyrics_response_when_error_raised():
    with pytest.raises(Exception) as e:
        parse_lyrics_response(response_data=None)

    assert isinstance(e.value,Exception)

def test_parse_lyrics_response_when_error_not_raised():
    response = parse_lyrics_response(data)
    assert isinstance(response,dict)

def test_song_lyrics_when_error_raised():
    with pytest.raises(Exception) as e:
        parse_song_lyrics(html_content=None)
    assert isinstance(e.value,Exception)

def test_song_lyrics_when_error_not_raised():
    html_content = parse_lyrics_response(data)
    response = parse_song_lyrics(html_content['html_content'])

    assert isinstance(response,list)

def test_quiz_preparation_when_database_lacks_artists():
    with pytest.raises(Exception) as e:
        MA.quiz_preparation(artists=None)

    assert str(e.value)== 'Not artists inside the database'

def test_quiz_preparation_when_artist_has_no_songs(mocker):
    mocker.patch('blitz_games_app.services.music_service.MusicService.artist_selector',
                 mocker.MagicMock(side_effect=IndexError))

    with pytest.raises(IndexError) as e:
        MA.quiz_preparation(artists = [10,11])

    assert isinstance(e.value,IndexError)


def test_quiz_preparation_when_lyrics_request_fails(mocker):
    mocker.patch('blitz_games_app.services.music_service.MusicService.artist_selector',
                 mocker.MagicMock(return_value=None))
    mocker.patch('blitz_games_app.services.music_service.MusicService.song_selector',
                 mocker.MagicMock(return_value=None))
    mocker.patch('blitz_games_app.utilities.utilities.get_song_lyrics',
                 mocker.MagicMock(return_value=None))

    with pytest.raises(Exception) as e:
        MA.quiz_preparation(artists=[10,11])

    assert isinstance(e.value,Exception)

def test_quiz_preparation_when_everything_works(mocker):
    mocker.patch('blitz_games_app.services.music_service.MusicService.artist_selector',
                 mocker.MagicMock(return_value=None))
    mocker.patch('blitz_games_app.services.music_service.MusicService.song_selector',
                 mocker.MagicMock(return_value=None))
    mocker.patch('blitz_games_app.services.music_service.get_song_lyrics',
                 mocker.MagicMock(return_value=None))
    mocker.patch('blitz_games_app.services.music_service.parse_lyrics_response',
                 mocker.MagicMock(return_value={'html_content':data}))

    mocker.patch('blitz_games_app.services.music_service.parse_song_lyrics',
                 mocker.MagicMock(return_value=None))
    mocker.patch('blitz_games_app.services.music_service.MusicService.verse_selector')

    # MA.quiz_preparation(artists=[69,170])

    # assert MA.song_title == '3 Wishes'
    # assert MA.artist == 'J. Cole'

