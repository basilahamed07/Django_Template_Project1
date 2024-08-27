from django.urls import  path
from . import views

urlpatterns = [
    path("", views.landing_page),
    path("images_form", views.ImageCreateView.as_view()),
    path("thankyou", views.thankyou),
    path("render_image",views.render_image),
    path("all-post", views.all_post, name="all-post"),
    path("<str:uniqe>", views.dataretrive, name="detail"),
    
] 
