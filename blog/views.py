from django.shortcuts import render

# Create your views here.


def allblogs(request):
    print('********+************************')
    print('in allblogs')
    print('********+************************')
    response = render(request, 'blog/allblogs.html')
    return response
