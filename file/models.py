from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
User=get_user_model()

def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.user.id, filename)



class user(User):
    file=models.FileField(upload_to=user_directory_path,null=True,blank=True)

