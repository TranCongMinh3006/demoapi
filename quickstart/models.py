from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, max_length=255)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     author = models.TextField()
#     category = models.CharField(max_length=255)

#     def get_absolute_url(self):
#         return reverse('blog_post_detail', args=[self.slug])

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super(Post, self).save(*args, **kwargs)

#     class Meta:
#         ordering = ['created_on']

#         def __unicode__(self):
#             return self.title


# class Comment(models.Model):
#     name = models.CharField(max_length=42)
#     email = models.EmailField(max_length=75)
#     website = models.URLField(max_length=200, null=True, blank=True)
#     content = models.TextField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)


# -----------------------------------------------------------------------------------------------------
class Articles(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()
    representation = models.TextField()
    displayContent = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    click_counter = models.IntegerField()
    slug = models.SlugField(unique=True, max_length=255)
    hot_score = models.IntegerField()

    def get_absolute_url(self):
        return reverse('blog_article_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Articles, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title


class Tags(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Article_Tags(models.Model):
    tagID = models.ForeignKey(Tags, on_delete=models.CASCADE)
    articleID = models.ForeignKey(Articles, on_delete=models.CASCADE)


class Categorys(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Article_Categorys(models.Model):
    categoryID = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    articleID = models.ForeignKey(Articles, on_delete=models.CASCADE)


class Comments(models.Model):
    articleID = models.ForeignKey(Articles, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class User_Views(models.Model):
    articleID = models.ForeignKey(Articles, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    time_view = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.time_view
