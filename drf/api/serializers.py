from rest_framework import serializers
from .models import customer,customer2

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'
class customerSerializer2(serializers.ModelSerializer):
    class Meta:
        model = customer2
        fields = '__all__'
    def validate_email(self, value):
        # Empty check
        if not value:
            raise serializers.ValidationError("Email field cannot be empty.")

        # Unique check
        if customer2.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")

        return value