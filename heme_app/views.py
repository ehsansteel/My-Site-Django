from django.shortcuts import render

from heme_app.models import User


def heme(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        topic = request.POST.get('topic')
        body = request.POST.get('body')
        view = request.POST.get('view')
        time = request.POST.get('time')
        User.objects.create(name=name, email=email, topic=topic, body=body, view=view, time=time)

    logo = User.objects.all().alias()

    return render(request, "heme_app/index.html", context={'login': logo},)
