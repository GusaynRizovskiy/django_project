from django.core.management import BaseCommand

from blogapp.models import Article,Author, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(f"Create article with author")
        author = Author.objects.get(name='Oscar Uaild')
        category = Category.objects.get(name="Clasic")
        artilce,created = Article.objects.get_or_create(
            title= "In horrible hospital",
            content = "In this place you are not human, you're monster",
            pub_date = "2023-02-13",
            author = author,
            category = category
        )
        artilce.save()
        self.stdout.write(f"Article was created")
