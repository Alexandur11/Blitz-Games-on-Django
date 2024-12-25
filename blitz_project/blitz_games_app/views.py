import pdb
import random

from django.shortcuts import render

from .models import Movie,Series,Artists
from .utilities.utilities import *
from .utilities.parsing_utilities import *
from .services.music_service import MusicService

MS = MusicService()
artists = Artists.objects.all()


def home_page(request):
    return render(request, 'home_page.html', {})


def movies_page(request):
    movies = Movie.objects.all()
    random_movie = random.choice(movies)
    return render(request, 'movie_page.html', {'random_movie':random_movie})

def tv_shows_page(request):
    tv_shows = Series.objects.all()
    random_tv_show = random.choice(tv_shows)
    return render(request,'series_page.html',{'random_tv_show':random_tv_show})

def music_page(request):

    songs = recursive_collection(None,1)
    songs_list = []
    for x in songs:
        if x:
            songs_list.extend(x)
    songs_list.pop()
    Artists(id=2,songs=songs_list).save()


    # MS.quiz_preparation(artists)







    return render(request, 'home_page.html', {})


cole = [599410, 4254003, 6808751, 5838250, 5838217, 354242, 3656498, 3753813, 3691852,
        3663828, 4674445, 3726621, 8306505, 104024, 1742597, 87297, 114703, 1975,
        5709850, 10179412, 146929, 2924190, 10245204, 10320953, 8404414,
        3207767, 6808753, 180979, 309069, 7725352, 8878884, 3039974, 164660, 3886292,
        791, 9042595, 9608854, 9404814, 9608855, 4155494, 4348344, 6809873,
        3351445, 527858, 8879059, 5636588, 10916034, 599442, 4254020, 6808745, 3955843, 58, 677,
        599407, 1786456, 4254008, 51425, 3658953, 192981, 8820261, 117, 52357, 3745000, 6866810,
        7148894, 675, 3674230, 1896, 496704, 622098, 53865, 2914474, 2021, 181167, 8568149,
        350105, 7787390, 2378981, 217104, 1869778, 11172039]


nas = [16507, 4032413, 92105, 6194925, 730650, 79279, 9312591, 6353283, 6353286, 760471, 6071906,
       8951488, 3429112, 9971091, 5428047, 8018789, 51942, 8988497, 704703,
       228375, 6627960, 10410280, 4013942, 741718, 689296, 670350, 2304945,
       7836999, 1246487, 201, 2896309, 4064434, 2934107, 1848417, 7110483, 1074900,
       704724, 2121104, 676184, 10410281, 689310, 74258, 27155, 16552, 7541151, 747166, 6928136,
       17178, 27173, 5600678, 704700, 27200, 83819, 50785, 9291540, 9291538, 8990257, 6046073,
       44965, 747117, 73080, 747124, 747165, 27188, 42253, 27189, 10451095, 6928122, 1815785,
       18557, 2670511, 60923, 27191, 1866305, 139, 4285732, 57588, 4007705, 689287, 11356, 43108,
       7315905, 9971088, 743421, 3767119]
