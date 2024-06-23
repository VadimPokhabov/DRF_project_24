from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """
    Сериализатор для модели Course
    """
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    """
    Сериализатор для модели Course
    """
    lesson_count = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        if obj.lesson.count():
            return obj.lesson.count()
        return 0


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
        fields = ('name', 'description', 'image', 'lesson', 'count_lesson')
