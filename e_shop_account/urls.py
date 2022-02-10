from django.urls import path

from .views import (login_user, register, log_out, user_account_main_page, edit_user_account, chang_user_password, user_likes, register_done)

urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register, name='register'),
    path('register-done', register_done),
    path('log_out', log_out),
    path('user', user_account_main_page, name='user_account'),
    path('user/edit', edit_user_account, name='user_edit'),
    path('user/edit_password', chang_user_password, name='user_password'),
    path('user/user_likes', user_likes, name='user_like'),
]
