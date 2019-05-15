from django.shortcuts import render
from .models import Images
# Create your views here.

def image_list(request):
	images=Images.objects.all()
	return render(request,'somi/image_list.html',{'images':images})
