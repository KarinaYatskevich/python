from django.urls import path
from .views import HomeNews, NewsByCategory, ViewNews, CreateNews, news_favourite_list, register, user_login, \
    favourite_news, user_logout, SearchResultsView, like_view

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    path('news/add-news', CreateNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('like/<int:pk>', like_view, name='like_news'),
    path('favourite_news/<int:pk>', favourite_news, name='favourite_news'),
    path('favourities/', news_favourite_list, name='news_favourite_list')

]
