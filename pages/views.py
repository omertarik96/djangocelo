from django.shortcuts import render


def home_view(request):
    """Render home page"""
    return render(request, "pages/home.html", {})


def course_detail_view(request):
    """Render course detail page"""
    return render(request, "pages/course_detail.html", {})
