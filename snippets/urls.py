from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet  #, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


"""URLs using Routers"""

router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="customuser")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]


"""URLs by View classes"""

# urlpatterns = [
#     # path("snippets/", views.snippet_list),
#     # path("snippets/<int:pk>/", views.snippet_detail),
#     path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
#     path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
#     path("users/", views.UserList.as_view(), name="customuser-list"),
#     path("users/<int:pk>/", views.UserDetail.as_view(), name="customuser-detail"),
#     path("", views.api_root),
#     path(
#         "snippets/<int:pk>/highlight/",
#         views.SnippetHighlight.as_view(),
#         name="snippet-highlight",
#     ),
# ]
#
# # */snippets.json, */snippets/2.json
# urlpatterns = format_suffix_patterns(urlpatterns)


"""
    Binding ViewSets to URLs explicitly
    
    The handler methods only get bound to the actions when we define the URLConf. 
    To see what's going on under the hood let's first explicitly create a set of views from our ViewSets.
"""

# snippet_list = SnippetViewSet.as_view(
#     {
#         "get": "list",
#         "post": "create",
#     }
# )
# snippet_detail = SnippetViewSet.as_view(
#     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
# )
# snippet_highlight = SnippetViewSet.as_view(
#     {"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer]
# )
# user_list = UserViewSet.as_view({"get": "list"})
# user_detail = UserViewSet.as_view({"get": "retrieve"})
#
# urlpatterns = format_suffix_patterns(
#     [
#         path("", api_root),
#         path("snippets/", snippet_list, name="snippet-list"),
#         path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
#         path(
#             "snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"
#         ),
#         path("users/", user_list, name="user-list"),
#         path("users/<int:pk>/", user_detail, name="user-detail"),
#     ]
# )
