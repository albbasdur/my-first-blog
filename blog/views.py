from django.shortcuts import render

# 20200307_ABD
def port_list(request):
    return render(request, 'blog/port_list.html', {})


