from django.shortcuts import render


# Create your views here.
def lobby(request):
    if request.method == 'POST':
        print('post')
    print(request.POST.get('message'))
    return render(request, 'chat/lobby.html')

from django.http import HttpResponse
from django.singlefile import SingleFileApp

app = SingleFileApp()


@app.path("")
def index(request):
    name = request.GET.get("name", "World")
    return HttpResponse(f"Hello, {name}!")


if __name__ == "__main__":
    app.main()