from rest_framework.serializers import ModelSerializer

from users.models import User, Payments


class PaymentsSerializer(ModelSerializer):
    """
    Сериализатор для модели Payments
    """
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(ModelSerializer):
    """
    Сериализатор для модели User
    """
    payment_history = PaymentsSerializer(source="payment_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
