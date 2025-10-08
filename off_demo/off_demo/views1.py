from django.http import HttpResponse

from django.views import View
from django.http import JsonResponse


def demo(request):
    # return HttpResponse("Hello function based view!")
    all_attrs = dir(request)
    #for collection: convert to str
    # return HttpResponse(f"<pre>{request.method}</pre>")
    data = {"a": 1, "b": 2}
    return JsonResponse(data)

class HomeView(View):
    def get1(self, request):
        return HttpResponse("Hello from get1 Class-Based View!")

