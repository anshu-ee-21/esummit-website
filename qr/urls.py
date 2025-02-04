from django.urls import path
from qr.views import *

app_name = 'qr'
urlpatterns = [
    path('', home, name='home'),
    path('profile', profile, name="profile"),
    path('scanner', scanner, name="scanner"),
    # # path('scan/', scan, name='scan'),
    path('result', leaderboard, name='leaderboard'),
    path('register', register, name='register_for_hunt'),
    path('scan/<slug:code>', scan, name='scan'), 
]