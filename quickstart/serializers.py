from django.contrib.auth.models import User, Group
from . models import Articles, Article_Categorys, Article_Tags, Tags, Categorys, Comments, User_Views
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['title', 'slug', 'content', 'created_on', 'author', 'category']

# class CommentSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['name', 'email', 'website', 'content', 'post', 'created_on']


#------------------------------------------------
class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articles
        fields = ['title', 'slug', 'link', 'representation','displayContent', 'content', 'created_on', 'click_counter', 'hot_score']


class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ['tag']

class Article_TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article_Tags
        fields = ['tagID', 'articleID']



class CategorysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorys
        fields = ['category']


class Article_CategorysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article_Categorys
        fields = ['categoryID', 'articleID']


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ['articleID', 'userID', 'content', 'created_on']


class User_ViewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Views
        fields = ['articleID', 'userID', 'time_view']