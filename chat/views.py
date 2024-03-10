from django.shortcuts import render


# Create your views here.
def lobby(request):
    if request.method == 'POST':
        print('post')
    print(request.POST.get('message'))
    return render(request, 'chat/lobby.html')
