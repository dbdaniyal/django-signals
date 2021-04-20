from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

# a receiving function which will do something 
# sender: model
# instance: obj of model
def save_post(sender, instance, **kwargs):
	print("\nsomething\n")

def after_delete_post(sender, instance, **kwargs):
	print("\ndeleted something\n")


# linking receiver to the actual receiver
# if sender is not specified then it wil take place after every single model is saved
pre_save.connect(save_post,sender=Post)
post_save.connect(save_post,sender=Post)
post_delete.connect(after_delete_post,sender=Post)
