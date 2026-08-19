from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Category, ProductType, ProductDetails

from .forms import ProductForm, ProductModelForm


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


    # ==========================================
    # QuerySet Functions - دوال الاستعلام
    # ==========================================

    # 1 - all()
    all_products = Product.objects.all()

    # 2 - filter()
    available_products = Product.objects.filter(
        available=True
    )

    # 3 - exclude()
    products_with_stock = Product.objects.exclude(
        quantity=0
    )

    # 4 - order_by()
    products_by_price = Product.objects.order_by(
        "price"
    )

    # 5 - values()
    product_names = Product.objects.values(
        "name",
        "price"
    )

    # 6 - count()
    products_count = Product.objects.count()

    # 7 - first()
    first_product = Product.objects.first()

    # بيانات المتجر
    store_name = "DentalStore"
    owner = "Jehan Adel"
    email = "jehan773@gmail.com"
    phone = "+967773455773"
    discount = 20

    # ===============================
    # مساعد متجر DentalStore
    # ===============================

    result = ""

    if request.method == "POST":

        symptom = request.POST.get("symptom", "").strip().lower()

        # تسوس
        if "تسوس" in symptom:
            result = """
الأدوات المقترحة:
• حفار الأسنان
• مادة الحشو
• جهاز التجفيف
• جهاز الأشعة
"""

        # ألم الأسنان
        elif "ألم" in symptom or "وجع" in symptom or "يوجع" in symptom:
            result = """
الأدوات المقترحة:
• مرآة الأسنان
• مسبار الأسنان
• جهاز الأشعة
• جهاز تنظيف الأسنان
"""

        # تورم وانتفاخ
        elif "تورم" in symptom or "انتفاخ" in symptom or "ورم" in symptom:
            result = """
الأدوات المقترحة:
• جهاز فحص الأسنان
• جهاز الأشعة
• أدوات علاج اللثة
• جهاز التعقيم
"""

        # تورم اللثة
        elif "تورم اللثة" in symptom or "انتفاخ اللثة" in symptom:
            result = """
الأدوات المقترحة:
• جهاز تنظيف اللثة
• أدوات اللثة
• غسول الفم
• جهاز إزالة الجير
"""

        # خراج
        elif "خراج" in symptom:
            result = """
الأدوات المقترحة:
• جهاز الأشعة
• أدوات علاج الجذور
• أدوات التعقيم
• مخدر موضعي
"""

        # ضرس العقل
        elif "العقل" in symptom:
            result = """
الأدوات المقترحة:
• جهاز الأشعة
• أدوات خلع الأسنان
• كماشة الخلع
"""

        # خلع
        elif "خلع" in symptom:
            result = """
الأدوات المقترحة:
• كماشة خلع الأسنان
• ملقط جراحي
• مخدر موضعي
• شاش طبي
"""

        # اللثة
        elif "لثة" in symptom:
            result = """
الأدوات المقترحة:
• جهاز تنظيف اللثة
• جهاز إزالة الجير
• أدوات اللثة
"""

        # نزيف
        elif "نزيف" in symptom:
            result = """
الأدوات المقترحة:
• شاش طبي
• أدوات اللثة
• جهاز التعقيم
"""

        # تنظيف الأسنان
        elif "تنظيف" in symptom:
            result = """
الأدوات المقترحة:
• جهاز تنظيف الأسنان
• فرشاة التلميع
• معجون التلميع
"""

        # جير
        elif "جير" in symptom:
            result = """
الأدوات المقترحة:
• جهاز إزالة الجير
• جهاز تنظيف الأسنان
"""

        # تقويم
        elif "تقويم" in symptom:
            result = """
الأدوات المقترحة:
• أدوات التقويم
• أسلاك التقويم
• قاطع الأسلاك
"""

        # ألم بعد التقويم
        elif "بعد التقويم" in symptom:
            result = """
الأدوات المقترحة:
• أدوات تعديل التقويم
• شمع التقويم
• أدوات الفحص
"""

        # حشو
        elif "حشو" in symptom or "حشوة" in symptom:
            result = """
الأدوات المقترحة:
• مادة الحشو
• حفار الأسنان
• جهاز التجفيف
"""

        # سقوط الحشوة
        elif "سقطت الحشوة" in symptom or "سقوط الحشوة" in symptom:
            result = """
الأدوات المقترحة:
• مادة الحشو
• جهاز تنظيف الحفرة
• أدوات الحشو
"""

        # كسر الأسنان
        elif "كسر" in symptom:
            result = """
الأدوات المقترحة:
• مواد ترميم الأسنان
• جهاز الأشعة
• أدوات الحشو
"""

        # حساسية
        elif "حساسية" in symptom or "بارد" in symptom or "ساخن" in symptom:
            result = """
الأدوات المقترحة:
• معجون علاج الحساسية
• أدوات الفحص
• جهاز الأشعة
"""

        # تبييض
        elif "تبييض" in symptom:
            result = """
الأدوات المقترحة:
• جهاز التبييض
• جل التبييض
• أدوات التجميل
"""

        # زرع الأسنان
        elif "زرع" in symptom:
            result = """
الأدوات المقترحة:
• أدوات زراعة الأسنان
• مثقاب الزراعة
• جهاز الأشعة
"""

        # أطفال
        elif "طفل" in symptom or "اطفال" in symptom:
            result = """
الأدوات المقترحة:
• أدوات أسنان الأطفال
• مرايا صغيرة
• جهاز تنظيف الأسنان
"""

        # فحص
        elif "فحص" in symptom:
            result = """
الأدوات المقترحة:
• مرآة الأسنان
• مسبار الأسنان
• جهاز الأشعة
"""

        # تجميل
        elif "تجميل" in symptom:
            result = """
الأدوات المقترحة:
• جهاز التبييض
• قشور الأسنان
• أدوات التجميل
"""

        # كرسي
        elif "كرسي" in symptom:
            result = """
الأجهزة المقترحة:
• كرسي الأسنان
• مصباح الأسنان
• وحدة الأسنان
"""

        # تعقيم
        elif "تعقيم" in symptom:
            result = """
الأدوات المقترحة:
• جهاز التعقيم
• أكياس التعقيم
• قفازات طبية
"""

        # أجهزة
        elif "جهاز" in symptom:
            result = """
الأجهزة المتوفرة:
• جهاز تنظيف الأسنان
• جهاز التعقيم
• جهاز الأشعة
• جهاز إزالة الجير
"""

        else:
            result = """
❌ لم أتعرف على الحالة.

جرب كتابة:
• ألم الأسنان
• تورم
• انتفاخ اللثة
• تسوس
• خراج
• ضرس العقل
• حشو
• خلع
• تقويم
• تنظيف
• جير
• تبييض
• حساسية
• زرع الأسنان
"""

    context = {
        "store_name": store_name,
        "owner": owner,
        "email": email,
        "phone": phone,
        "discount": discount,
        "products": products,
        "result": result,

        # QuerySet
        "all_products": all_products,
        "available_products": available_products,
        "products_with_stock": products_with_stock,
        "products_by_price": products_by_price,
        "product_names": product_names,
        "products_count": products_count,
        "first_product": first_product,
    }

    return render(request, "products/home.html", context)


# ==========================================
# Form 1 - HTML Form
# ==========================================

def product_form_html(request):

    result = ""

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        price = request.POST.get("price", "").strip()

        if not name or not price:

            result = "يرجى تعبئة جميع الحقول."

        else:

            result = f"تم إدخال المنتج: {name} - السعر: {price}$"

    return render(
        request,
        "products/product_form_html.html",
        {
            "result": result
        }
    )


# ==========================================
# Form 2 - Django Forms.Form
# ==========================================

def product_form_django(request):

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]
            price = form.cleaned_data["price"]

            return render(
                request,
                "products/product_form_django.html",
                {
                    "form": form,
                    "success": f"تم استقبال المنتج: {name} - السعر: {price}$"
                }
            )

    else:

        form = ProductForm()

    return render(
        request,
        "products/product_form_django.html",
        {
            "form": form
        }
    )


# ==========================================
# Form 3 - ModelForm
# ==========================================

def product_form_modelform(request):

    if request.method == "POST":

        form = ProductModelForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect("product_list")

    else:

        form = ProductModelForm()

    return render(
        request,
        "products/product_form_modelform.html",
        {
            "form": form
        }
    )


# ==========================================
# QuerySet Page
# ==========================================

def querysets_view(request):

    # 1 - all()
    all_products = Product.objects.all()

    # 2 - filter()
    available_products = Product.objects.filter(
        available=True
    )

    # 3 - exclude()
    products_with_stock = Product.objects.exclude(
        quantity=0
    )

    # 4 - order_by()
    products_by_price = Product.objects.order_by(
        "price"
    )

    # 5 - values()
    product_names = Product.objects.values(
        "name",
        "price"
    )

    # 6 - count()
    products_count = Product.objects.count()

    # 7 - first()
    first_product = Product.objects.first()

    return render(
        request,
        "products/querysets.html",
        {
            "all_products": all_products,
            "available_products": available_products,
            "products_with_stock": products_with_stock,
            "products_by_price": products_by_price,
            "product_names": product_names,
            "products_count": products_count,
            "first_product": first_product,
        }
    )


# ==========================================
# One To One Relationship
# ==========================================

def one_to_one_view(request):

    product = Product.objects.first()

    if product is None:

        return render(
            request,
            "products/one_to_one.html",
            {
                "message": "لا يوجد منتجات في قاعدة البيانات."
            }
        )

    details = ProductDetails.objects.filter(
        product=product
    ).first()

    if request.method == "POST":

        manufacturer = request.POST.get(
            "manufacturer",
            ""
        ).strip()

        warranty = request.POST.get(
            "warranty",
            ""
        ).strip()

        specifications = request.POST.get(
            "specifications",
            ""
        ).strip()

        if details:

            details.manufacturer = manufacturer
            details.warranty = warranty
            details.specifications = specifications

            details.save()

        else:

            ProductDetails.objects.create(
                product=product,
                manufacturer=manufacturer,
                warranty=warranty,
                specifications=specifications
            )

        return redirect("one_to_one")

    return render(
        request,
        "products/one_to_one.html",
        {
            "product": product,
            "details": details
        }
    )


# ==========================================
# Many To Many Relationship
# ==========================================

def many_to_many_view(request):

    product = Product.objects.first()

    product_types = ProductType.objects.all()

    if product is None:

        return render(
            request,
            "products/many_to_many.html",
            {
                "message": "لا يوجد منتجات في قاعدة البيانات.",
                "product_types": product_types
            }
        )

    if request.method == "POST":

        selected_types = request.POST.getlist(
            "product_types"
        )

        product.product_types.set(
            selected_types
        )

        return redirect("many_to_many")

    selected_types = product.product_types.all()

    selected_ids = [
        item.id
        for item in selected_types
    ]

    return render(
        request,
        "products/many_to_many.html",
        {
            "product": product,
            "product_types": product_types,
            "selected_ids": selected_ids
        }
    )


# ==========================================
# CRUD - Read
# ==========================================

def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        "products/product_list.html",
        {
            "products": products
        }
    )


# ==========================================
# CRUD - Create
# ==========================================

def product_create(request):

    if request.method == "POST":

        form = ProductModelForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect("product_list")

    else:

        form = ProductModelForm()

    return render(
        request,
        "products/product_form.html",
        {
            "form": form,
            "title": "إضافة منتج"
        }
    )


# ==========================================
# CRUD - Update
# ==========================================

def product_update(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if request.method == "POST":

        form = ProductModelForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            form.save()

            return redirect("product_list")

    else:

        form = ProductModelForm(
            instance=product
        )

    return render(
        request,
        "products/product_form.html",
        {
            "form": form,
            "title": "تعديل المنتج"
        }
    )


# ==========================================
# CRUD - Delete
# ==========================================

def product_delete(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if request.method == "POST":

        product.delete()

        return redirect("product_list")

    return render(
        request,
        "products/product_confirm_delete.html",
        {
            "product": product
        }
    )