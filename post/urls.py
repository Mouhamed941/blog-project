from django.urls import path
from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.PostList.as_view(),name="post_list"),
    path('login/', include("django.contrib.auth.urls"),name="login"),
    path('logout/',views.logout,name="logout"),
    path("post_detail/<int:pk>/",views.PostDetail, name="post_detail"),
    path("edite_comment/<str:pk>/",views.edit_comment, name="edit_comment"),
    path("delete_comment/<str:pk>/",views.delete_comment, name="delete_comment"),
    
]
