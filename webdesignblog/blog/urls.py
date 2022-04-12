from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search/', views.inlineSearch, name='search'),
    path('like/', views.likePost, name='like'),
    path('detail/<slug:post_slug>', views.post_detail, name='detail'),
    path('detail/comment/', views.comments, name="comment"),
    path("category/<slug:category_slug>/", views.category_list, name='category_list')
]
# paths    