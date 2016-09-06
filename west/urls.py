from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'west.views.first_page'),
    url(r'^staff/', 'west.views.staff'),
    url(r'^templay/', 'west.views.templay'),
]