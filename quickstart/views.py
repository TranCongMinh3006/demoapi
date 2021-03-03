from django.shortcuts import render
from django.contrib.auth.models import User, Group
from . models import Articles, Article_Tags, Tags, Article_Categorys, Categorys, User_Views, Comments
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import ArticlesSerializer, UserSerializer, GroupSerializer, Article_CategorysSerializer, CategorysSerializer, Article_TagsSerializer, TagsSerializer, User_ViewsSerializer, CommentsSerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArticlesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

    @action(detail=False)
    def thethao(self, request):
        thethao = Articles.objects.filter(article_categorys__categoryID=1)

        # thethao = Article_Categorys.objects.filter(categoryID='the thao')

        page = self.paginate_queryset(thethao)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(thethao, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def new_article(self, request):
        new_article = Articles.objects.all().order_by('-created_on',)

        page = self.paginate_queryset(new_article)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(new_article, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def hot_article(self, request):
        number_of_articles = Articles.objects.all().count()
        weight_score = 3
        for i in range(1,number_of_articles+1):
            click_score = Articles.objects.all()[i-1].click_counter
            number_of_commnents = Comments.objects.filter(articleID=i).count()
            hot_score1 =number_of_commnents*weight_score + click_score
            Articles.objects.filter(id = i).update(hot_score=hot_score1)

        hot_article = Articles.objects.all().order_by('-hot_score',)

        page = self.paginate_queryset(hot_article)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(hot_article, many=True)
        return Response(serializer.data)


class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CategorysViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Categorys.objects.all()
    serializer_class = CategorysSerializer


class Article_CategorysViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article_Categorys.objects.all()
    serializer_class = Article_CategorysSerializer


class TagsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class Article_TagsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article_Tags.objects.all()
    serializer_class = Article_TagsSerializer


class User_ViewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User_Views.objects.all()
    serializer_class = User_ViewsSerializer