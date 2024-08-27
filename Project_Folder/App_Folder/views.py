from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView

# Create your views here.
def landing_page(request):
    latest_data = Post.objects.all().order_by("-time")[0:3]
    return render(request,"App_Folder/landingpage.html",{"data":latest_data})

def all_post(request):
    data = Post.objects.all()
    return render(request,"App_Folder/all-post.html",{"data":data})

def dataretrive(request,uniqe):
    posts = Post.objects.get(slug=uniqe)
    return render(request,"App_Folder/post_details.html",{"data":posts})


def thankyou(request):
    return render(request,"App_Folder/thankyou.html")


def render_image(request):
    image_object = Post.objects.all()
    return render(request,"App_Folder/image_render.html",{"image_object":image_object})

class ImageCreateView(CreateView):
    model = Post
    template_name = "App_Folder/image_form.html"
    success_url = "thankyou"
    fields = "__all__"
