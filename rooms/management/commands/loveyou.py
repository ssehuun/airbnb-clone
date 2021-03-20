from django.core.management.base import BaseCommand


class Command(BaseCommand):
    print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many time do you want me to tell you that I love u",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            # print("i love you")
            self.stdout.write(self.style.ERROR("I love you"))
