from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.HomeView.as_view() , name='homePage'),
    path('detile_article/<int:pk>', v.DetilePostView.as_view(), name='detile-post'),
    path('add_article', v.AddPostCreateView.as_view(), name='add-post'),
    path('My_article', v.MyPostView.as_view(), name='my-post'),
    path('update_article/edit/<int:pk>', v.UpdatePostView.as_view(), name='edit-post'),
    path('delete_aticle/<int:pk>/remove', v.DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cat>/', v.CategoryView, name='category-view'),
    path('category/menu', v.CategoryListView, name='category-list'),
    path('like/<int:pk>', v.LikeView, name='like'),
    path('<int:pk>/detile_profile/', v.ShowDetileProfileView.as_view(), name='show-detile-profile'),
    path('article/add_comments/<int:pk>', v.AddCommentsView.as_view(), name='add-comment'),
    path('serch_page/', v.SearchView, name='search-page' ),
]