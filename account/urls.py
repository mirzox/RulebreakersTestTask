from django.urls import path


from .views import LoginView, Logout

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', Logout.as_view()),
]