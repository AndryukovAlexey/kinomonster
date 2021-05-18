from django.contrib import admin
from .models import Movies, Serials, News, Comments, Likes

admin.site.register(Movies)
admin.site.register(Serials)
admin.site.register(News)
admin.site.register(Comments)
admin.site.register(Likes)

