from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),  # SignUpView.as_view() → signup に変更
    # 他のURL設定...
]