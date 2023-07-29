from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path("snippets/", views.snippet_list),
    # path("snippets/<int:pk>/", views.snippet_detail),
    path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),

    path("users/", views.UserList.as_view(), name="customuser-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="customuser-detail"),

    path("", views.api_root),

    path("snippets/<int:pk>/highlight/", views.SnippetHighlight.as_view(), name="snippet-highlight"),
]

# */snippets.json, */snippets/2.json
urlpatterns = format_suffix_patterns(urlpatterns)