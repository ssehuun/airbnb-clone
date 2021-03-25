import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from rooms import models as room_models
from users import models as user_models

NAME = "lists"


class Command(BaseCommand):
    help = "This command creates f{NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many f{NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            list_models.List, number, {"user": lambda x: random.choice(users)}
        )
        created = seeder.execute()
        cleaned = flatten(created.values())
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.room.add(*to_add)  # queryset안의 값들을 가져오기 위애 * 사용

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
