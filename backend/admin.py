from django.contrib import admin
from backend.models import (
    User,
    Shop,
    Category,
    Order,
    OrderItem,
    Contact,
    ConfirmEmailToken,
    ProductParameter,
    ProductInfo,
    Product,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = [
        "date_joined",
        "is_staff",
        "groups",
        "user_permissions",
        "is_superuser",
        "last_login",
    ]


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "state", "user")
    list_filter = ("state",)
    search_fields = ("name",)
    list_editable = ("state",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)
    save_on_top = True


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    model = ProductParameter
    extra = 0


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    model = ProductInfo
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "dt", "state", "contact")
    list_filter = ("state",)
    save_on_top = True
    date_hierarchy = "dt"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    extra = 0


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(ConfirmEmailToken)
class ConfirmEmailTokenAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "key",
        "created_at",
    )
