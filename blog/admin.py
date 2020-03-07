from django.contrib import admin
from .models import Post

# 20200307_ABD
# The model is registered for making it visible in the admin page
admin.site.register(Post)

