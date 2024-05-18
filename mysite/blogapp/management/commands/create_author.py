from django.core.management import BaseCommand

from blogapp.models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        author_names = [
            ("Dghonson Boris","Young author"),
            ("Oscar Uaild", "Famous author in our world"),
            ("John Smith", "If you don't know who it, you've some problem")
        ]
        for author_name in author_names:
            Author.objects.get_or_create(name=author_name[0],bio=author_name[1])
            self.stdout.write(f"Create author {author_name[0]}")
        self.stdout.write(f"Authors were created")

