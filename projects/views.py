from django.shortcuts import render, get_object_or_404, redirect
from .models import Project

def project_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    projects = Project.objects.all()

    if query:
        projects = projects.filter(title__icontains=query)

    if category:
        projects = projects.filter(category__iexact=category)

    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)

    # if project.is_private and not request.user.is_authenticated:
    #     return redirect('/admin/login/?next=' + request.path)

    # ✅ Split tech stack into list
    tech_list = [tech.strip() for tech in project.tech_stack.split(',') if tech.strip()]

    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tech_list': tech_list,
    })