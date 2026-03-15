from projects.models import Project
from skills.models import Skill
from blog.models import BlogPost
from .models import ContactMessage
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from collections import defaultdict

def dashboard(request):
    context = {
        'project_count': Project.objects.count(),
        'blog_count': BlogPost.objects.count(),
        'message_count': ContactMessage.objects.count(),
        'featured_count': Project.objects.filter(featured=True).count(),
    }
    return render(request, 'core/dashboard.html', context)

def home(request):
        # Featured projects
    featured_projects = Project.objects.filter(featured=True)[:3]

    # Latest blog posts
    posts = BlogPost.objects.filter(published=True)[:3]

    # Group skills by category
    skills = Skill.objects.all().order_by("category", "-level")

    return render(request, 'core/home.html', {
        'projects': featured_projects,
        'posts': posts,
        "skills": skills,
    })

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Basic validation
        if not name or not email or not message:
            messages.error(request, "Please fill all fields.")
            return redirect('/contact/')

        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email (fail silently so site never crashes)
        try:
            send_mail(
                subject=f"New Portfolio Message from {name}",
                message=f"From: {email}\n\n{message}",
                from_email=None,  # uses DEFAULT_FROM_EMAIL
                recipient_list=['yourgmail@gmail.com'],
                fail_silently=True,
            )
        except Exception:
            pass

        messages.success(request, "Message sent successfully! I’ll get back to you soon.")
        return redirect('/contact/')

    return render(request, 'core/contact.html')