from django.shortcuts import render, redirect
from .models import (
    Teacher, Course, Testimonial, TimeSlot, Booking,
    PricingPlan, Progress, BlogPost, ContactMessage
)
from django.contrib.auth.decorators import login_required


def home(request):
    testimonials = Testimonial.objects.all()
    return render(request, "home.html", {"testimonials": testimonials})

def book_course(request):
    return render(request, 'book_course.html')

def about(request):
    teacher = Teacher.objects.first()
    return render(request, "about.html", {"teacher": teacher})


def courses(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})


def booking(request):
    courses = Course.objects.all()
    slots = TimeSlot.objects.all()

    if request.method == "POST":
        Booking.objects.create(
            name=request.POST["name"],
            age=request.POST["age"],
            course_id=request.POST["course"],
            slot_id=request.POST["slot"],
            payment_method=request.POST["payment_method"],
        )
        return redirect("home")

    return render(request, "booking.html", {"courses": courses, "slots": slots})


def pricing(request):
    plans = PricingPlan.objects.all()
    return render(request, "pricing.html", {"plans": plans})


@login_required
def progress(request):
    user_progress = Progress.objects.filter(student=request.user)
    return render(request, "progress.html", {"progress": user_progress})


def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, "testimonials.html", {"testimonials": testimonials})


def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            message=request.POST["message"],
        )
        return redirect("home")
    return render(request, "contact.html")


def blog(request):
    posts = BlogPost.objects.all()
    return render(request, "blog.html", {"posts": posts})


def blog_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog_detail.html", {"post": post})


from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Course, Teacher

@staff_member_required
def add_course_ajax(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        age_group = request.POST.get("age_group")
        level = request.POST.get("level", "")
        price_per_month = request.POST.get("price_per_month", 0)
        duration_weeks = request.POST.get("duration_weeks", 4)

        course = Course.objects.create(
            title=title,
            description=description,
            age_group=age_group,
            level=level,
            price_per_month=price_per_month,
            duration_weeks=duration_weeks
        )

        return JsonResponse({
            "success": True,
            "course": {
                "title": course.title,
                "description": course.description,
                "age_group": course.age_group,
                "level": course.level,
                "price_per_month": str(course.price_per_month),
                "duration_weeks": course.duration_weeks
            }
        })

    return JsonResponse({"success": False})

