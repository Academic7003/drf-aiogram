from django.urls import path, include
from comments.api.views import *

urlpatterns = [
    path('get-users', get_users),
    path('get-user', get_user),
    path('get-user-language', get_user_lang),
    path('get-ratings', get_ratings),
    path('get-rating', get_rating),
    path('get-ratinger', get_ratinger),
    path('add-rating', add_rating),
    path('add-ratinger', add_ratinger),
    path('get-user-given-ratings', get_user_given_ratings),
    path('add-user', add_user),
    path('add-lang', add_lang),
    path('add-phone', add_phone_ratinger),
    path('add-photo-to-user', add_photo_to_user),
    path('del-rating', delete_user_ratings),
    path('get-jobs', get_jobs),
    path('get-sort-user', get_sort_users_job),
    path('get-ratinger-raitings', get_ratinger_raitings),
    path('get-user-raitinger-direction', get_user_raitinger_direction),
    path('get-all-users', get_all_users),


]