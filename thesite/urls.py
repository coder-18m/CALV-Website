from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, DevelopmentView, DevelopmentMapView, TransportMapView, SchoolsMapView, SampleLetterView, FireView, EditView, LikeView, AddCommentView

urlpatterns = [
    path('', views.index, name='index'),
    path('developsum/', DevelopmentView.as_view(), name="developsum"),
    path('developmap/', DevelopmentMapView.as_view(), name="developmap"),
    path('transportmap/', TransportMapView.as_view(), name="transportmap"),
    path('schoolsmap/', SchoolsMapView.as_view(), name='schoolsmap'),
    path('sampleleter/', SampleLetterView.as_view(), name="sampleleter"),
    path('contact/', views.contact, name="contact"),
    path('fire/', FireView.as_view(), name="fire"),
    path('editletter/', EditView.as_view(), name="editletter"),

    #path('home/', views.home, name='home'),
    path('home/', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/edit/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
]
