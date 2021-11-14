from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from photo.models import Photo


class HomeView(View):
    def get(self, request):
        photos = Photo.objects.all()
        paginator = Paginator(photos,5)
        page_num = request.GET.get('page')
        photos = paginator.get_page(page_num)

        return render(request, 'index.html', locals())

    def post(self, request):
        photos = Photo.objects.all()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # 登入
        if user is not None and user.is_superuser:
            login(request, user)
        # 登出
        isLogout = request.POST.get('isLogout')
        if isLogout == 'True':
            logout(request)
        return render(request, 'index.html', locals())


# def HomeView(request):
#     photos = Photo.objects.all()
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         # 登入
#         if user is not None and user.is_superuser:
#             login(request, user)
#         # 登出
#         isLogout = request.POST.get('isLogout')
#         if isLogout == 'True':
#             logout(request)
#     return render(request, 'index.html', locals())


class UploadView(View):
    def get(self, request):
        pass

    def post(self, request):
        if request.user.is_superuser:
            images = request.FILES.getlist('images')
            for image in images:
                Photo.objects.create(image=image)
        return redirect(reverse('photo:index'))
