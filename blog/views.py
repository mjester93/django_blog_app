from django.shortcuts import render

posts = [
    {
        'author': 'Michael Jester',
        'title': 'Writing My First Django Application',
        'content': 'first post content',
        'date_posted': 'September 19, 2020'
    },
    {
        'author': 'John Smith',
        'title': 'Post #2',
        'content': 'Here is my second post!',
        'date_posted': 'September 20, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }

    return render(request, 'blog/about.html', context)
