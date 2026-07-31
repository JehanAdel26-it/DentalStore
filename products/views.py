from django.shortcuts import render


def home(request):

    # قائمة المنتجات (متغير محلي)
    products = [
        {
            "name": "جهاز تنظيف الأسنان",
            "price": 120,
            "stock": 15,
            "category": "الأجهزة"
        },
        {
            "name": "كرسي الأسنان",
            "price": 950,
            "stock": 4,
            "category": "الكراسي"
        },
        {
            "name": "جهاز التعقيم",
            "price": 280,
            "stock": 0,
            "category": "التعقيم"
        },
        {
            "name": "مرآة الأسنان",
            "price": 18,
            "stock": 22,
            "category": "الأدوات"
        }
    ]

    # بيانات المتجر (متغيرات محلية)
    store_name = "DentalStore"
    owner = "Jehan Adel"
    email = "jehan773@gmail.com"
    phone = "+967773455773"
    discount = 20

    context = {
        "store_name": store_name,
        "owner": owner,
        "email": email,
        "phone": phone,
        "discount": discount,
        "products": products,
    }

    return render(request, "products/home.html", context)