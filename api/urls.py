from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView



urlpatterns = [
    path('api/',views.StudentDetails.as_view()),
    path('api/<int:pk>',views.StudentDetails.as_view()),
    path('gettoken/',TokenObtainPairView.as_view(), name='token_generator'),
    path('tokenrefresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('tokenverify/',TokenVerifyView.as_view(), name='token_verify'),
]



# referesh token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5Nzc5ODExMywiaWF0IjoxNjk3NzExNzEzLCJqdGkiOiJhZWQ4MjFlNmI0NTQ0M2IzOTljZTU3ODliZWU0ZDNhOSIsInVzZXJfaWQiOjJ9.7XBVPJloP5zKZrBnxknfGTWgBdpvTV-KW1pGbz0somI" 
# access token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3NzEyMDEzLCJpYXQiOjE2OTc3MTE3MTMsImp0aSI6ImEyZDY1YTdkYzhjZDQ0OTk5ZTI5ZGI0YTAwYTE5MjNjIiwidXNlcl9pZCI6Mn0.o9grwRFS6Tfs3EWmaZyb-Mzxmj-_eikBYW-vnM4c_XU"
