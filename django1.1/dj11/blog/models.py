from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

##############################################################
'''
one implementation: making tag a separate entity
then we can sort by pairing the tag with the post
I also thought of making it a weak entity but that is 
too much fuss andd this way we will be able to add
some popularity statistic to the tags later.
'''
# class Tag(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
##############################################################



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #uncomment to check the first implementation
    #tags = models.ManyToManyField(Tag)
    tags = TaggableManager()

    def __str__(self):
        return self.title
