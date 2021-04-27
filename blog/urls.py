from django.urls import path, include
from . import views
from AccountReg import views as v
from .views import BlogCreateView, BlogUpdateView, BlogDeleteView, AddCommentView

urlpatterns = [
path("", views.index, name='index'),
path("post/", views.allPosts, name="listpost"),
path("post/<int:pk>/", views.detailedView, name="fullPost"),
path("post/new/", BlogCreateView.as_view(), name="newpost"),
path("post/<int:pk>/comment", AddCommentView.as_view(), name="newcomment"),
path('register/', v.register, name='register' ),
# path('post/login/', v.register, name='login' ),
path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="edit"),
path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="delete"),
]

