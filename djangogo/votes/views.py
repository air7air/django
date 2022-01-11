from django.shortcuts import render
from django.http import HttpResponse

def view_all_polls(request):
    method = request.method
    name = request.GET.get('name','username') # 이름이 있으면 이름이 나오고 아무것도 입력 안하고 polls만 입력하면 username이 나옴
    if method == 'GET':
        data = request.GET.urlencode()
    if method == 'POST':
        data = request.POST.urlencode()

    return HttpResponse("method: %s data: %s" % (method, name))

def create_polls(request):
    return HttpResponse("create")

def view_poll_by_id(request, id):
    return HttpResponse("view"+str(id))

def vote_poll(request, id):
    return HttpResponse("vote poll"+str(id))

def update_poll(request, id):
    return HttpResponse("update pol"+str(id))

def delete_poll(request, id):
    return HttpResponse("delete poll"+str(id))
