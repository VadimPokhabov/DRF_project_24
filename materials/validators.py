from rest_framework.exceptions import ValidationError


class URLValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = value.get(self.field)
        if reg and not reg.startswith("https://www.youtube.com/"):
            raise ValidationError("site is not ok")
