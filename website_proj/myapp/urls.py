from django.urls import path
from myapp import views

# urlpatterns = [
#     path('input/', views.text_input, name='text_input'),
# ]

urlpatterns = [
    path('', views.text_input, name='text_input'),
]

# urlpatterns = [
#     path("", views.index, name="index"),
# ]
