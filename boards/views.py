from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, '
                        ' 1'
                        ' 2'
                        ' 3'
                        ' 4'
                        ' 5'
                        'World!')