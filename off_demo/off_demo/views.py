from django.shortcuts import render,redirect,get_object_or_404
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
    
    # var_name = "salman md sultan1"
    # var_email = "salman12@gmail.com"
    # var_phone = "011"
    # c = models.Customer1(name=var_name,email=var_email,phone=var_phone)
    # c.save()


    # create_customer = c.objects.create(name=var_name,email=var_email,phone=var_phone)
    # customer_list = [c(name="alomgi",email='a@gmailcom',phone='01'),c(name='piash',email='piash@gmail.com',phone='03'), c(name='oni',email='oni@gmail.com',phone='123')]

    # create_customer_bulk = c.objects.bulk_create(customer_list)


    #save function
    # data = {'d':['salman','sultan']}
    return render(req,'customer.html')
def course(req):
    customer = models.Customer1
    all_data = customer.objects.all() #queryset
    all_data_dic = {'data':all_data}
    print(all_data)
    return render(req,'course.html',all_data_dic)
def demo_function_show(req):
    customer = models.Customer1
    all_data = customer.objects.all() #queryset
    all_data_dic = {'data':all_data}
    print(all_data)
    return render(req,'demo.html',all_data_dic)

def course_show(req):
    course = models.Course
    all_data = course.objects.all() #queryset
    all_data_dic = {'data':all_data}
    print(all_data)
    return render(req,'course_show.html',all_data_dic)


def course_insert(req):
    customer = models.Customer1
    
    cus_id = req.POST.get('customer')
    course_name = req.POST.get('cus_name')
    price = req.POST.get('number')
    cus = get_object_or_404(customer, id=cus_id)
    course= models.Course(name = course_name,price = price,cus_id=cus)
    course.save()
    return redirect('show_course')
def customer(req):

    customer_name = req.POST.get('cus_name')
    email = req.POST.get('email')
    phone = req.POST.get('phone')
    file = req.FILES.get('file')
    Customer1= models.Customer1(name = customer_name,email = email,phone = phone,file=file)
    Customer1.save()
    return redirect('show_customer')

def edit(req,id):
    # customer = models.Customer1
    customer = get_object_or_404(models.Customer1, id=id) #queryset
    return render(req,'customer_edit.html',{'data':customer})

def customer_update(req):
    customer = get_object_or_404(models.Customer1, id=req.POST.get('cus_id'))

    if req.method == 'POST':
        customer_name = req.POST.get('cus_name')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        file = req.FILES.get('file')

        # Update field values
        customer.name = customer_name
        customer.email = email
        customer.phone = phone
        if file:  # যদি নতুন file আসে তখন আপডেট হবে
            customer.file = file

        customer.save()  # Database update
        return redirect('show_customer') 
    
def customer_edit(req,cid):
    customer = models.Customer1
    cust_data = get_object_or_404(customer,id=cid)
    data = {'d':cust_data}
    return render(req,'customer_edit_form.html',data)
    # return HttpResponse(cid)
def customer_update1(req):
    cus_id = req.POST.get('cus_id')
    customer_name = req.POST.get('cus_name')
    email = req.POST.get('email')
    phone = req.POST.get('phone')
    file = req.FILES.get('file')
    customer = models.Customer1
    cust_data = get_object_or_404(customer,id=cus_id)
    
    cust_data.name = customer_name
    cust_data.email = email
    cust_data.phone = phone
    if file:
        cust_data.file = file
    cust_data.save()
    return redirect('show_customer')