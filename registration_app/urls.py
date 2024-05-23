from django.urls import path
from registration_app.views import RegisterView, LoginView, UploadImagesView, UserImagesView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('upload-images/', UploadImagesView.as_view(), name='upload-images'),
    path('user-images/', UserImagesView.as_view(), name='user-images'),
]
