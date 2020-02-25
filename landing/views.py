from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import PhotoForm
from .models import Photo
# Create your views here.


class HomePageView(TemplateView):

    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        photos = Photo.objects.all()
        context = {
            "landing_name": "Maria Portfolio",
            'photos': photos
        }
        return context


# def gallery(request):
#     photos = Photo.objects.all()
#     return render(request, 'landing/gallery.html', {'photos': photos})


# def upload_photo(request):
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = PhotoForm()
#     return render(request, 'landing/upload_photo.html', {'form': form})


class PhotoListView(ListView):
    model = Photo
    template_name = 'landing/gallery.html'
    context_object_name = 'photos'


class UploadPhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('landing:gallery')
    template_name = 'landing/upload_photo.html'


def delete_photo(request, pk):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=pk)
        photo.delete()
    return redirect('landing:gallery')

