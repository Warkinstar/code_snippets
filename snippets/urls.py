from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("snippets/", views.snippet_list),
    path("snippets/<int:pk>/", views.snippet_detail),
]

# */snippets.json, */snippets/2.json
urlpatterns = format_suffix_patterns(urlpatterns)