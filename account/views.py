from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

from .models import UserAccount, Profile


# ==============================
# تسجيل حساب جديد
# ==============================

def register(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name", "").strip()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        password = request.POST.get("password", "")
        address = request.POST.get("address", "").strip()

        # التحقق من الحقول
        if not full_name or not username or not email or not phone or not password:

            messages.error(
                request,
                "يرجى تعبئة جميع الحقول المطلوبة."
            )

            return redirect("account_register")

        # التحقق من اسم المستخدم
        if UserAccount.objects.filter(username=username).exists():

            messages.error(
                request,
                "اسم المستخدم موجود مسبقاً."
            )

            return redirect("account_register")

        # التحقق من البريد
        if UserAccount.objects.filter(email=email).exists():

            messages.error(
                request,
                "البريد الإلكتروني مستخدم مسبقاً."
            )

            return redirect("account_register")

        # إنشاء الحساب
        user = UserAccount.objects.create(

            full_name=full_name,

            username=username,

            email=email,

            phone=phone,

            password=make_password(password),

            address=address

        )

        # ==========================================
        # إنشاء Profile للمستخدم
        # علاقة One To One
        # ==========================================

        Profile.objects.create(
            user=user
        )

        # حفظ بيانات المستخدم في Session
        request.session["user_id"] = user.id

        messages.success(
            request,
            "تم إنشاء الحساب بنجاح."
        )

        return redirect("account_profile")

    return render(
        request,
        "account/register.html"
    )


# ==============================
# تسجيل الدخول
# ==============================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username", "").strip()

        password = request.POST.get("password", "")

        try:

            user = UserAccount.objects.get(
                username=username
            )

        except UserAccount.DoesNotExist:

            messages.error(
                request,
                "اسم المستخدم أو كلمة المرور غير صحيحة."
            )

            return redirect("account_login")

        # التحقق من حالة الحساب
        if not user.is_active:

            messages.error(
                request,
                "هذا الحساب غير نشط."
            )

            return redirect("account_login")

        # التحقق من كلمة المرور
        if check_password(password, user.password):

            request.session["user_id"] = user.id

            messages.success(
                request,
                "تم تسجيل الدخول بنجاح."
            )

            return redirect("account_profile")

        else:

            messages.error(
                request,
                "اسم المستخدم أو كلمة المرور غير صحيحة."
            )

            return redirect("account_login")

    return render(
        request,
        "account/login.html"
    )


# ==============================
# الملف الشخصي
# ==============================

def profile(request):

    user_id = request.session.get("user_id")

    if not user_id:

        messages.warning(
            request,
            "يجب تسجيل الدخول أولاً."
        )

        return redirect("account_login")

    try:

        user = UserAccount.objects.get(
            id=user_id
        )

    except UserAccount.DoesNotExist:

        request.session.flush()

        return redirect("account_login")

    # ==========================================
    # الحصول على Profile المرتبط بالمستخدم
    # ==========================================

    try:

        profile_data = user.profile

    except Profile.DoesNotExist:

        profile_data = Profile.objects.create(
            user=user
        )

    return render(
        request,
        "account/profile.html",
        {
            "user": user,
            "profile": profile_data
        }
    )


# ==============================
# تسجيل الخروج
# ==============================

def logout_view(request):

    request.session.flush()

    messages.success(
        request,
        "تم تسجيل الخروج بنجاح."
    )

    return redirect("account_login")