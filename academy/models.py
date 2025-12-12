from django.db import models
from django.contrib.auth.models import User


AGE_LEVELS = [
    ('4-7', '4-7'),
    ('8-12', '8-12'),
    ('13-18', '13-18'),
    ('adult', 'Adult'),
]


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    qualifications = models.TextField(blank=True)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)

def __str__(self):
    return self.full_name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null=True, blank=True)
    contact_number = models.CharField(max_length=30, blank=True)
    parent_name = models.CharField(max_length=200, blank=True)


def __str__(self):
    return self.full_name

class Certification(models.Model):
    teacher = models.ForeignKey(Teacher, related_name="certifications", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    age_group = models.CharField(max_length=20, choices=AGE_LEVELS)
    level = models.CharField(max_length=100, blank=True)
    price_per_month = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    duration_weeks = models.PositiveIntegerField(default=4)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)


def __str__(self):
    return self.title

class TimeSlot(models.Model):
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    video = models.FileField(upload_to='lessons/videos/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)


class Meta:
    ordering = ['order']


def __str__(self):
    return f"{self.course.title} - {self.title}"

class Booking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slot_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    payment_completed = models.BooleanField(default=False)


def __str__(self):
    return f"Booking: {self.student} for {self.course} at {self.slot_datetime}"

class PricingPlan(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    provider = models.CharField(max_length=100, blank=True)
    transaction_id = models.CharField(max_length=200, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)


def __str__(self):
    return f"Payment {self.amount} for {self.booking}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Progress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    percent_complete = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"{self.student} - {self.course} ({self.percent_complete}%)"


class Testimonial(models.Model):
    student_name = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"Testimonial by {self.student_name}"


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)


def __str__(self):
    return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title