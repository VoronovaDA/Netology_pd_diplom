# Верстальщик
from rest_framework import serializers

from backend.models import (
    User,
    Parameter,
    Category,
    Shop,
    ProductInfo,
    Product,
    ProductParameter,
    OrderItem,
    Order,
    Contact,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "last_name",
            "first_name",
            "surname",
            "email",
            "password",
            "company",
            "type",
            "position",
        ]
        extra_kwargs = {"password": {"write_only": True}}


class LoginAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=150)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "id",
            "city",
            "street",
            "house",
            "structure",
            "building",
            "apartment",
            "user",
            "phone",
        )
        read_only_fields = ("id",)
        extra_kwargs = {"user": {"write_only": True}}

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return Contact.objects.create(**validated_data)


class ConfirmAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(max_length=150)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "products")
        read_only_fields = ("id",)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            "id",
            "name",
            "state",
        )
        read_only_fields = ("id",)


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = (
            "name",
            "category",
        )


class ParameterSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Parameter
        fields = (
            "name",
            "category",
        )


class ProductParameterSerializer(serializers.ModelSerializer):
    parameter = serializers.StringRelatedField()

    class Meta:
        model = ProductParameter
        fields = (
            "parameter",
            "value",
        )


class ProductInfoSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_parameters = ProductParameterSerializer(read_only=True, many=True)

    class Meta:
        model = ProductInfo
        fields = (
            "id",
            "model",
            "product",
            "shop",
            "quantity",
            "price",
            "price_rrc",
            "product_parameters",
        )
        read_only_fields = ("id",)


class PartnerStateSerializer(serializers.Serializer):
    state = serializers.BooleanField()


class PartnerUpdateSerializer(serializers.Serializer):
    file = serializers.FileField()


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product_info",
            "quantity",
            "order",
        )
        read_only_fields = ("id",)
        extra_kwargs = {"order": {"write_only": True}}


class OrderItemCreateSerializer(OrderItemSerializer):
    product_info = ProductInfoSerializer(read_only=True)


class OrderSerializer(serializers.ModelSerializer):
    ordered_items = OrderItemCreateSerializer(read_only=True, many=True)

    total_sum = serializers.IntegerField()
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "ordered_items",
            "state",
            "dt",
            "total_sum",
            "contact",
        )
        read_only_fields = ("id",)
