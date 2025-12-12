from django.contrib import admin
from .models import Teacher, Student, Course, Lesson, Booking, Payment, Progress, Testimonial, BlogPost


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name','experience_years')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name','age','contact_number')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','age_group','price_per_month','teacher')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title','course','order')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('student','course','slot_datetime','confirmed')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking','amount','provider','paid_at')


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('student','course','percent_complete','last_update')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('student_name','created_at')


# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title','created_at','published')