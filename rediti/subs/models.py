from django.db import models
from common.models import IndexedTimeStampModel


class Subred(model.Models):
    title = models.CharField(max_length=50)
    creator = models.ForeignKey("users.User", related_name="Subreds", on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title
    

class Thread(model.Models):
    title = models.CharField(max_length=50)
    author = models.ForeignKey("users.User", related_name="threads", on_delete=models.CASCADE)
    Subred = models.ForeignKey('Subred', related_name="threads", on_delete=models.CASCADE)
    vote_count = models.IntegerField(default=0)

    class Meta:
        ordering = -['created']

    def __str__(self):
        return self.title
    
class Post(model.Models):
    content = models.TextField()
    author = models.ForeignKey("users.User", related_name="posts", on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', related_name="posts", on_delete=models.CASCADE)
    vote_count = models.IntegerField(default=0)

    class Meta:
    ordering = ['created']

    def __str__(self):
        return ("{} - {} - {}").format(self.id, self.thread, self.author)


class Subscription(IndexedTimeStampedModel):
    user = models.ForeignKey('users.User', related_name=subscription, on_delete=models.CASCADE)
    sub = models.ForeignKey('Subred', related_name=subscription, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)

    class Meta:
        unique_together = [('user', 'sub')]