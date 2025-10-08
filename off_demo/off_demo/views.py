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
from . import models
def demo_function1(req):
    
    var_name = "salman md sultan1"
    var_email = "salman1@gmail.com"
    var_phone = "011"
    c = models.Customer1(name=var_name,email=var_email,phone=var_phone)
    c.save()


    # create_customer = c.objects.create(name=var_name,email=var_email,phone=var_phone)
    # customer_list = [c(name="alomgi",email='a@gmailcom',phone='01'),c(name='piash',email='piash@gmail.com',phone='03'), c(name='oni',email='oni@gmail.com',phone='123')]

    # create_customer_bulk = c.objects.bulk_create(customer_list)


    #save function
    data = {'d':['salman','sultan']}
    return render(req,'demo.html',data)

def demo_function_show(req):
    customer = models.Customer1
    all_data = customer.objects.all() #queryset
    all_data_dic = {'data':all_data}
    print(all_data)
    return render(req,'demo.html',all_data_dic)