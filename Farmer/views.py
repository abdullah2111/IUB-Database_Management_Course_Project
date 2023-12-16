from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import userFrom
from .models import Cart
from django.shortcuts import get_object_or_404
from Supplier.models import sTable
from Product.models import pTable
from Farmer.models import fTable
from Order.models import oTable
from testserver.models import bug2
from LandingPage.models import User


# Create your views here.



# Start
def bugg(loggedinperson):
    bug_instance, created = bug2.objects.get_or_create(id=784)
    if not created:
        bug_instance.user = loggedinperson
        bug_instance.save() 
    else:
        bug2.objects.create()



bugg("FarmerNormal")


def get_supplier_by_username(email):
    supplier = get_object_or_404(User, email=email)
    print(supplier.pk)
    bugg(supplier.pk)

def get_user_by_username(username):
    supplier = get_object_or_404(User, username=username)
    get_supplier_by_username(supplier.email)


def dataPassingOverSeasFarmer(username):
    # print(username)
    get_user_by_username(username)

# End






def base(request):
    return render(request, ('Farmer/base.html'))

def page_view(request):
    return render(request, ('Farmer/index.html'))

def priceOffer(request):
    return render(request, ('Farmer/priceOffer.html'))

def consultancy(request):
    return render(request, ('Farmer/consultancy.html'))
   
   

# def order(request):
#     total = 0
#     data = {}
#     cart_items = Cart.objects.all()
#     supplier_model = supplier.objects.all()
#     product_model = product.objects.all()

#     data['product_model'] = product_model
#     data['supplier_model'] = supplier_model

#     try:
#         if request.method == 'POST':
#             supp = request.POST['supplier_type']
#             pro = request.POST['product_name']
#             quantity = int(request.POST['quantity'])

            

#             selected_product = product.objects.get(productName=pro)
            

#             total = quantity * selected_product.productPrice
#             print(total)

#             # Add the new item to the cart
#             Cart.objects.create(
#                 supplier=supp,
#                 product=pro,
#                 quantity=quantity,
#                 totalPrice=total
#             )
#             data['cart_items'] = cart_items

#     except Exception as e:
#         print(e)

#     delivery_charge = 50
#     final_total = delivery_charge + total

#     data['total'] = total
#     data['delivery_charge'] = delivery_charge
#     data['final_total'] = final_total


#     return render(request, 'mainSite/order.html', data)

gsuppID = 0
gproID = 0
gquanity =0
gtotal = 0
def order(request):
    global gsuppID, gproID, gquanity, gtotal
    total = 0
    data = {}
    cart_items = Cart.objects.all()
    supplier_model = sTable.objects.all()
    product_model = pTable.objects.all()

    data['product_model'] = product_model
    data['supplier_model'] = supplier_model
    product_list = []

    try:
       
        if request.method == 'POST':
            action = request.POST.get('action')

            if action == 'add_to_cart':
                # Add to Cart logic
                supp = request.POST['supplier_type']
                
               
                pro = request.POST['product_name']
                quantity = int(request.POST['quantity'])
                gquanity = quantity



                

                selected_product = pTable.objects.get(productName=pro)
                selected_supplier = sTable.objects.get(supplierType=supp)
                gsuppID = selected_supplier.supplierID
                gproID = selected_product.productID 
                print(gsuppID, gproID)
                product_list = pTable.objects.filter(supplierID=gsuppID)

                product_list1 = [order.productName for order in product_list]

                data['product_model'] = product_list1

                total = quantity * selected_product.productPrice

                gtotal = total

                # Add the new item to the cart
                Cart.objects.create(
                    supplier=supp,
                    product=pro,
                    quantity=quantity,
                    totalPrice=total
                )
                

            elif action == 'place_order':
                Cart.objects.all().delete()

                gfarmerID = 0
                bug_instance, created = bug2.objects.get_or_create(id=784) 
                supp_instance, created = sTable.objects.get_or_create(supplierID=gsuppID) 
                pro_instance, created = pTable.objects.get_or_create(productID=gproID) 
        
                if  bug_instance.user == 'FarmerNormal':
                    pass 
                else:
                    f_table_instance, f_table_created = fTable.objects.get_or_create(farmerID=bug_instance.user)
                    gfarmerID = f_table_instance.farmerID

                gfarmerIDins, created = fTable.objects.get_or_create(farmerID=gfarmerID) 
                
                

                print(gsuppID, gproID, gfarmerID, gquanity)
                print(supp_instance.supplierID)

                add =''
                home = request.POST['home']
                street = request.POST['street']
                zip = request.POST['zip']
                city = request.POST['city']
                add += home+street+zip+city

                oTable.objects.create(
                    supplierID=supp_instance,
                    productID=pro_instance,
                    farmerID=gfarmerIDins,
                    orderDate=request.POST['order_date'],
                    quantity=gquanity,
                    totalPrice = gtotal,
                    address = add,
                )
                
                print(gsuppID, gproID, gfarmerID, gquanity)
               
                

                
                
               

    except Exception as e:
        print(e)

    delivery_charge = 50
    final_total = delivery_charge + total


    data['cart_items'] = cart_items
    data['total'] = total
    data['delivery_charge'] = delivery_charge
    data['final_total'] = final_total

    return render(request, 'Farmer/order.html', data)



def form(request):
    fn = userFrom()
    result = 0
    data = {'form': fn}
    try:
        if request.method == 'POST':
         s1 = int(request.POST['num1'])
         s2 = int(request.POST['num2'])
         result = s1 + s2
         data = {"form": fn,
                  "output":result}
        
        
    except:
        pass

    
    return render(request, 'mainSite/h.html',data)



