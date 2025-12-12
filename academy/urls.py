from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("courses/", views.courses, name="courses"),
    path("booking/", views.booking, name="booking"),
    path("pricing/", views.pricing, name="pricing"),
    path("progress/", views.progress, name="progress"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path('book-course/', views.book_course, name='book_course'),
    path("courses/add-ajax/", views.add_course_ajax, name="add_course_ajax"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
]
