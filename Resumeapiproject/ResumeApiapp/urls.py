from django.urls import path
from ResumeApiapp import views
urlpatterns = [
    path('addresume/',views.add_resume_view),
]
