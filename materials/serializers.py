from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import URLValidator


class LessonSerializer(ModelSerializer):
    """
    Сериализатор для модели Course
    """

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [URLValidator(field="url")]


class CourseSerializer(ModelSerializer):
    """
    Сериализатор для модели Course
    """

    lesson_count = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, obj):
        if obj.lesson.count():
            return obj.lesson.count()
        return 0

    def get_subscription(self, instance):
        request = self.context.get('request')
        user = None
        if request:
            user = request.user
        return instance.subscription_set.filter(user=user).exists()


class CourseDetailSerializer(ModelSerializer):
    """
    Сериализатор для модели детального просмотра course
    """

    lesson = LessonSerializer(many=True)
    count_lesson = SerializerMethodField()

    def get_count_lesson(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Course
        fields = ("course_name", "description", "image", "lesson", "count_lesson")


class SubscriptionSerializer(ModelSerializer):
    """
    Сериализатор для модели подписки
    """

    class Meta:
        model = Subscription
        fields = "__all__"
