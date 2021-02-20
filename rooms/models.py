from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models  # User db와 연결


class AbstratItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstratItem):
    pass


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # host는 User db와 연결해야 하기 때문에 Foreign key 필요
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # RoomType 은 Entire, Private, Hotel, Shared 이 됨
    room_type = models.ManyToManyField(RoomType, blank=True)

    def __str__(self):
        return self.name
