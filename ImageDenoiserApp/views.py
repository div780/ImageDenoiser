
from django.shortcuts import render, redirect

from .models import ImageModel

image_i=0

def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        uploaded_image = ImageModel(image=image)
        uploaded_image.save()
        return redirect('home', image_id=uploaded_image.id)
    return render(request, 'upload.html')

def home(request, image_id):
    image_i=image_id
    image = ImageModel.objects.get(id=image_i)

    return render(request, 'home.html', {'image': image})

def meanFilter(request):
    image = ImageModel.objects.get(id=image_i)
   
    return render(request, 'meanFilter.html',{'image': image})

def button2_view(request):
    return render(request, 'button2.html')

def button3_view(request):
    return render(request, 'button3.html')
