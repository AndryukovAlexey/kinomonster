from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from users import views as usersView
from django.contrib.auth import views as AuthViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('reg/', usersView.registr, name='reg-page'),
    path('update-profile/', usersView.update_profile, name='profile-update'),
    path('update-password/', usersView.update_password, name='password-update'),
    path('reg/conf/', usersView.conf, name='conf-page'),
    path('support/', usersView.support_user, name='cont-page'),
    #path('accounts/', include('allauth.urls')),
    path('accounts/', include('social_django.urls')),
    path('login/', usersView.Log.as_view(template_name='users/login.html'),name='login-page'),
    path('logout/', AuthViews.LogoutView.as_view(), name='logout-page'),
    #path('bill/', usersView.buy_premium, name='pay-page'),
    path('check_order/', usersView.check_order, name='check-page'),
    path('order/success/', usersView.order_success, name='success-page'),
    re_path(r'^(?P<username>\w+)/$', usersView.UserDetailView.as_view(), name='profile'),
]

handler404 = 'movies.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
