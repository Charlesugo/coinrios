import os
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', 'jpeg']
    if ext.lower() in valid_extensions:
        if filesize > 2621440:
            raise ValidationError("Upload an image with The maximum size of 2.5MB!")
        else:
            return value
    else:
        raise ValidationError(u'Unsupported file extension.')

