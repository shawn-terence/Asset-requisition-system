from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path("user/register/", UserRegistrationView.as_view(), name="register"),
    path("user/login/", UserLoginView.as_view(), name="login"),
    path("assets/add/", AssetAddView.as_view(), name="add_asset"),
    path(
        "user/updatepassword/", UserUpdatePasswordView.as_view(), name="update_password"
    ),
    path("user/userdetails/", UserDetailView.as_view(), name="user_details"),
    path("user/changeRole/", ChangeUserRoleView.as_view(), name="change_role"),
    path('user/<int:user_id>/delete/', DeleteUserView.as_view(), name='delete_user'),
    path("user/allusers/", AllUsersView.as_view(), name="all_users"),
    path("assets/allassets/", AssetListView.as_view(), name="all_assets"),
    path(
        "assets/<int:asset_id>/request/",
        AssetUpdateView.as_view(),
        name="request asset",
    ),
    path("assets/<int:asset_id>/delete/",AssetDeleteView.as_view(),name="delete_asset"),
    path("requests/", RequestListView.as_view(), name="request_list"),
    path(
        "requests/<int:request_id>/", RequestActionView.as_view(), name="request_action"
    ),
]
