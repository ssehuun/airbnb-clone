from django.db import models


class TimeStampedModel(models.Model):
    """ Time Stamped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:  # TimeStampedModel 모델이 데이베이스에는 나타나지 않게 설정
        abstract = True