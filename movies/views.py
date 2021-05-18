from django.shortcuts import render, redirect, get_object_or_404
from .models import Movies, Serials, News, Comments
from django.views.generic import ListView, DetailView
from django.views import View
from itertools import chain
from .forms import Comment
from .models import Comments, Likes
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, resolve
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

news = News.objects.order_by('-date')[:3]
rat_movie = Movies.objects.order_by('-rating')[:6]

def error_404(request, exception):
    return render(request, 'movies/404.html', {'title': title, 'news': news, 'rat_movie': rat_movie})

class HomeListView(ListView):
   
    model = Movies
    template_name = 'movies/index.html'
    context_object_name = 'movies'
    

    def get_context_data(self, **kwargs):
        ctx = super(HomeListView, self).get_context_data(**kwargs)
        ctx['title'] = 'main page'
        ctx['serials'] = Serials.objects.all()
        ctx['news'] = news
        ctx['rat_movie'] = rat_movie
        return ctx

class FilmListView(ListView):
       
    model = Movies
    template_name = 'movies/films.html'
    context_object_name = 'films'
    paginate_by = 3

    def get_queryset(self):
        return Movies.objects.order_by('-year')
    

    def get_context_data(self, **kwargs):
        ctx = super(FilmListView, self).get_context_data(**kwargs)
        ctx['title'] = 'films page'
        ctx['news'] = news
        
        ctx['rat_movie'] = rat_movie
        return ctx

class SerialsListView(ListView):
       
    model = Serials
    template_name = 'movies/serials.html'
    context_object_name = 'serials'
    paginate_by = 3

    def get_queryset(self):
        return Serials.objects.order_by('-year')
    

    def get_context_data(self, **kwargs):
        ctx = super(SerialsListView, self).get_context_data(**kwargs)
        ctx['title'] = 'serials page'
        ctx['news'] = news
        
        ctx['rat_movie'] = rat_movie
        return ctx

class AddReview(View):

    def post(self, request, pk):
        movie = None
        serial = None
        current_url = resolve(request.path_info).url_name
        form = Comment(request.POST)
        if current_url == 'film_add_review':      
            movie = Movies.objects.get(id=pk)
        elif current_url == 'serial_add_review':
            serial = Serials.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.avatar = request.user.profile.avatar
            if movie:
                form.movie = movie
            elif serial:
                form.serial = serial
            
            form.user = request.user
            form.save()
        
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class MoviePageListView(DetailView):
    model = Movies
    template_name = 'movies/show.html'
    context_object_name = 'movie_pg'
    
    def post(self, request, pk):
        movie = Movies.objects.get(id=pk)
        if 'like' in request.POST:
            like = Likes                         
            like.objects.create(user=request.user, movie=movie, name=movie.title)
        elif 'unlike' in request.POST:
            like = Likes.objects.get(user=request.user, movie=movie)
            like.delete()
        return redirect(request.path_info)

    def get_context_data(self, **kwargs):
        ctx = super(MoviePageListView, self).get_context_data(**kwargs)
        ctx['news'] = news
        ctx['likes'] = Likes.objects.filter(movie=self.object).count()
        ctx['form'] = Comment
        if self.request.user.is_authenticated:
            ctx['like_mov'] = Likes.objects.filter(user=self.request.user, movie=self.object)          
        ctx['comm'] = Comments.objects.all()
        ctx['rat_movie'] = rat_movie
        return ctx

class SerialPageListView(DetailView):
    model = Serials
    template_name = 'movies/show.html'
    context_object_name = 'serial_pg'

    def post(self, request, pk):
        serial = Serials.objects.get(id=pk)
        if 'like' in request.POST:
            like = Likes                         
            like.objects.create(user=request.user, serial=serial, name=serial.title)
        elif 'unlike' in request.POST:
            like = Likes.objects.get(user=request.user, serial=serial)
            like.delete()
        return redirect(request.path_info)

    def get_context_data(self, **kwargs):
        ctx = super(SerialPageListView, self).get_context_data(**kwargs)
        # ctx['title'] = f'page {title}'
        ctx['news'] = news
        ctx['form'] = Comment
        ctx['abiba'] = Group.objects.get(name="abiba")
        if self.request.user.is_authenticated:
            ctx['like_ser'] = Likes.objects.filter(user=self.request.user, serial=self.object)
        ctx['comm'] = Comments.objects.all()
        ctx['rat_movie'] = rat_movie
        return ctx


def rating_mov(request):
    query = list()
    res_query = list()
    query1 = list()

    mov = Movies.objects.order_by('rating')
    ser = Serials.objects.order_by('rating')

    for i in range(len(mov)):
        mo = mov[i]
        query.append(mo.rating)
    for i in range(len(ser)):
        se = ser[i]
        query.append(se.rating)

    for i in range(len(query)):
        lowest = i

        for j in range(i+1, len(query)):
            if query[j] < query[lowest]:
                lowest = j

        query[i],  query[lowest] = query[lowest], query[i]

    query.reverse()
        
    for i in query:
        query1.append(i)

    for i in query1:
        if query1.count(i) > 1:
            query1.remove(i)


    for i in query1:
        

        m = Movies.objects.filter(rating=i)

        s = Serials.objects.filter(rating=i)

        if m  is not None:
            res_query.append(m)

        if s is not None:
            res_query.append(s)   

    return render(request, 'movies/rating.html', {'ratin': res_query, 'title': 'rating', 'news': news, 'rat_movie': rat_movie})

def search(request):
    search_query = request.GET.get('q', '')
    search_user = str(search_query).title()
    title = 'Поиск'
    if search_query:
        movie = Movies.objects.filter(title__icontains=search_user)
        serial = Serials.objects.filter(title__icontains=search_user)
        if movie or serial:
            return render(request, 'movies/search.html', {'mov': movie, 'ser': serial, 'title': title, 'news': news, 'rat_movie': rat_movie})
        else:
           return render(request, 'movies/search.html', {'mist': 'У нас нет такого(', 'title': title, 'news': news, 'rat_movie': rat_movie}) 
    else:
        movie = Movies.objects.all()
        serial = Serials.objects.all()
    
        return render(request, 'movies/search.html', {'mov': movie, 'ser': serial, 'title': title, 'news': news, 'rat_movie': rat_movie})
    

