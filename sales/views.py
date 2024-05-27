from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request , 'index.html')

# def products(request):
#     phones = ['apple', 'huawei', 'samsung', 'infinix', 'oppo']
#     context = {'products': phones, 
#                'cust_name': 'John'
#                }
#     return render(request , 'products.html', context)

def boot(request):
    return render(request , 'boot.html')

def customers(request):

    customers = [
        {'name': 'John',
         'phone': '+254750000000',
         'email': 'john@gmail,com'},
        {
            'name': 'Jane',
            'phone': '+254750000001',
            'email': 'jane@gmail,com'
        },
        {
            'name': 'Doe',
            'phone': '+254750000002',
            'email': 'doe@gmail,com'
        },
        {
            'name': 'kim',
            'phone': '+254750000002',
            'email': 'kim@gmail,com'
        },
    ]
    context = {'customers': customers}
    return render(request , 'customers.html', context)

def products(request):
    tvs = [
        {'brand': 'sony',
         'price': 50000,
         'size': 32,
         'in_store': 9
         },
         
        {
            'brand': 'skyworth',
            'price': 50000,
            'size': 42,
            'in_store': 11,
        },
        {
            'brand': 'samsung',
            'price': 60000,
            'size': 42,
            'in_store': 8,
        },
        {
            'brand': 'lg',
            'price': 70000,
            'size': 52,
            'in_store': 10,
        },
        {
            'brand': 'hisense',
            'price': 80000,
            'size': 62,
            'in_store': 7,
        },
        {
            'brand': 'skywave',
            'price': 90000,
            'size': 72,
            'in_store': 9,
        }
    ]
    context = {'tvs': tvs}
    return render(request , 'products.html', context)
