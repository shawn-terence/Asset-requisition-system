"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from api.views import*

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("addasset/",AssetAddView.as_view(),name="add_asset"),
    path("updatepassword/",UserUpdatePasswordView.as_view(),name="update_password"),
    path("ChangeRole/",ChangeUserRoleView.as_view(),name="change role"),
    path("deleteUser/",DeleteUserView.as_view(),name="delete user"),
    path("getallusers/",AllUsersView.as_view(),name="get all users"),
    path("getallassets/",AssetListView.as_view(),name="get all assets"),
    path("assets/<int:asset_id>/request/",AssetUpdateView.as_view(),name="request asset"),
    path('requests/', RequestListView.as_view(), name='request-list'),
    path('requests/<int:request_id>/', RequestActionView.as_view(), name='request-action')
]
