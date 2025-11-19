from rest_framework import serializers
from .models import customer,customer2
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'
class customerSerializer2(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=False,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    class Meta:
        model = customer2
        fields = '__all__'
        # extra_kwargs = {
        #     "password": {"write_only": True}
        # }
    def validate_email(self, value):
        # Empty check
        if not value:
            raise serializers.ValidationError("Email field cannot be empty.")

        # Unique check
        if customer2.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")

        return value
    # def validate_password(self, value):
    #     validate_password(value)
    #     return value
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        validated_data['is_active'] = True  # default
        validated_data['is_staff'] = False
        validated_data['is_superuser'] = False
        return super().create(validated_data)