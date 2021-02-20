from django.db import models


class TimeStampedModel(models.Model):
    """ Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """ TimeStampedModel 모델이 데이베이스에는 나타나지 않고 추상모델로 설정 """

        abstract = True
