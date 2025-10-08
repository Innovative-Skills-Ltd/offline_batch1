from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models


# def demo_function(req):
#     # print("hello world")
#     # all_attr = dir(req)

#     # data = {"a": 1, "b": 2}
#     # return HttpResponse(f"<pre>{req.method}</pre>")
#     Customer1= models.Customer1

#     # Insert multiple rows
#     Customer1.objects.bulk_create([
#     Customer1(name="Ayesha", email="ayesha2@gmail.com", phone=22),
#     Customer1(name="Hasan", email="hasan2@yahoo.com", phone=30),
#     Customer1(name="Nusrat", email="nusrat2@gmail.com", phone=28),
#     ])

#     c1 = Customer1(name="Ayesha", email="ayesha1@gmail.com", phone=22)
#     c1.save()

#     # 2nd customer
#     c2 = Customer1(name="Hasan", email="hasan1@yahoo.com", phone=30)
#     c2.save()

#     # 3rd customer
#     c3 = Customer1(name="Nusrat", email="nusrat1@gmail.com", phone=28)
#     c3.save()
#     context = {'message': 'This message is coming from Django backend!'}
#     return render(req, 'demo.html', context)

# def show(req):
#     Customer1= models.Customer1

#     customers = Customer1.objects.all()
#     print(list(customers.values()))
#     context = {
#         'customers': customers
#     }

#     return render(req, 'demo.html', context)

def demo_function1(req):
    data = {'d':['salman','sultan']}
    return render(req,'demo.html',data)