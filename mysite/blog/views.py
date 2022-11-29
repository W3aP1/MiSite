from django.shortcuts import render

def post_line(request):
    return render(request, 'blog/post_line.html', {})
