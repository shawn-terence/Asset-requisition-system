

from django.contrib import admin
from django.urls import path
from api.views import*

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/register/", UserRegistrationView.as_view(), name="register"),
    path("user/login/",UserLoginView.as_view(),name="login"),
    path("assets/add/",AssetAddView.as_view(),name="add_asset"),
    path("user/updatepassword/",UserUpdatePasswordView.as_view(),name="update_password"),
    path("user/changeRole/",ChangeUserRoleView.as_view(),name="change role"),
    path("user/deleteUser/",DeleteUserView.as_view(),name="delete user"),
    path("user/allusers/",AllUsersView.as_view(),name="get all users"),
    path("assets/allassets/",AssetListView.as_view(),name="get all assets"),
    path("assets/<int:asset_id>/request/",AssetUpdateView.as_view(),name="request asset"),
    path('requests/', RequestListView.as_view(), name='request-list'),
    path('requests/<int:request_id>/', RequestActionView.as_view(), name='request-action')
]
