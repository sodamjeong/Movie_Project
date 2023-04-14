from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def main(request):
    url = 'https://www.megabox.co.kr/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.select('.main-movie-list .list > li')
    rank = 1
    movie_list = {}
    for movie in movies:
        img_url = movie.select_one('.poster')['src']
        title = movie.select_one('.poster')['alt']
        rating = movie.select_one('.number').text
        movie_list[rank] = [img_url, title, rating]
        rank += 1
        if rank == 5:
            break
    context = {
        'movie_list' : movie_list,
    }
    return render(request, 'main.html', context)