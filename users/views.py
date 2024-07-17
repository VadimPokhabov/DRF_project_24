from django.views.generic import DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson
from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer
from users.services import create_stripe_product, create_stripe_price, create_stripe_session, checkout_session


class UserViewSet(ModelViewSet):
    """
    ViewSet для модели User
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [AllowAny]
        return super().get_permissions()


class PaymentsListAPIView(ListAPIView):
    """
    API для получения списка уроков
    """

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("course", "lesson", "payment_method")
    ordering_fields = ("payment_date",)


class PaymentsCreateAPIView(generics.CreateAPIView):
    """
    Payment create endpoint.
    """
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        """
        Привязывает платеж (с использованием stripe) к пользователю.
        """
        instance = serializer.save()
        instance.user = self.request.user

        course_id = self.request.data.get('course')
        lesson_id = self.request.data.get('lesson')
        if course_id:
            course_product = create_stripe_product(Course.objects.get(pk=course_id).course_name)
            course_price = create_stripe_price(instance.course.amount, course_product)
            session_id, payment_link = create_stripe_session(course_price)
        else:
            lesson_product = create_stripe_product(Lesson.objects.get(pk=lesson_id).lesson_name)
            lesson_price = create_stripe_price(instance.lesson.amount, lesson_product)
            session_id, payment_link = create_stripe_session(lesson_price)

        payment_status = checkout_session(session_id)
        instance.payment_status = payment_status
        instance.session_id = session_id
        instance.payment_link = payment_link
        instance.save()


class PaymentDetailView(DetailView):
    """
    Представление об оплате
    """
    model = Payments
