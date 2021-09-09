import time
import base64
import webcolors
from django.core.files.base import ContentFile
from rest_framework import serializers


class Base64ToContentFileField(serializers.Field):
    """Accepts base64-encoded string and returns navite django file instance.
    """
    def to_representation(self, value):
        return value.url if value else None

    def to_internal_value(self, data):
        try:
            _, base64_string = data.split(';base64,')
            return ContentFile(
                content=base64.b64decode(base64_string),
                name=f'{time.time()}.webp'
            )
        except Exception:
            raise serializers.ValidationError(
                'Failed to convert base64-string to an image.'
            )


class HEXToColourNameField(serializers.Field):
    """Accepts a colour name as hexadecimal representation and returns
    human-readable text.
    """
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            return webcolors.hex_to_name(data)
        except Exception:
            raise serializers.ValidationError(
                'There is no such colour name.'
            )