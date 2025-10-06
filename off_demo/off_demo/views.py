
from django.http import HttpResponse, JsonResponse
def demo_function(req):
    print("hello world")
    all_attr = dir(req)

    data = {"a": 1, "b": 2}
    return HttpResponse(f"<pre>{req.method}</pre>")