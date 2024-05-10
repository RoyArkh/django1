from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from taggit.managers import TaggableManager

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        
        for tag in self.tags.all():
            tag_obj, created = Tag.objects.get_or_create(name=tag.name)
            if created:
                self.tags.add(tag_obj)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
