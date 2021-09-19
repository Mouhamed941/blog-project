from django.urls import path

from . import views
app_name = 'my_app'
urlpatterns = [
    path('',views.HorseList.as_view(),name="template_view"),
    path('horse_detail/<str:pk>/',views.HorseDetail.as_view(),name="horse_detail"),
    # path('second',views.second_view,name="second_view"),
]
