from django.shortcuts import render

# Create your views here.
def post_list(request):
    # Ваш код здесь
    return render(request, 'blog/post_list.html', {})

