from django.shortcuts import render
from django.contrib.auth.models import User, Group
from . models import Post, Comment
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import UserSerializer, GroupSerializer, PostSerializer , CommentSerializer
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


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False)
    def thethao(self, request):
        thethao = Post.objects.filter(category='the thao')

        page = self.paginate_queryset(thethao)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(thethao, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def new_article(self, request):
        new_article = Post.objects.all().order_by('-created_on',)[:100]

        page = self.paginate_queryset(new_article)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(new_article, many=True)
        return Response(serializer.data)

# class PostViewSetCategory(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Post.objects.filter(category='thoi su')
#     serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



#--------------------------------------------------------------------


# from django.contrib.auth.models import User
# from . serializers import UserSerializer
# from rest_framework import generics
# from rest_framework.permissions import IsAdminUser

# class UserList(viewsets.ViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]

#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def get_queryset(self):
#         user = self.request.user
#         return user.objects.all()
    
    # def get_object(self):
    #     queryset = self.get_queryset()
    #     filter = {}
    #     for field in self.multiple_lookup_fields:
    #         filter[field] = self.kwargs[field]

    #     obj = get_object_or_404(queryset, **filter)
    #     self.check_object_permissions(self.request, obj)
    #     return obj

    # def filter_queryset(self, queryset):
    #     filter_backends = [CategoryFilter]

    #     if 'geo_route' in self.request.query_params:
    #         filter_backends = [GeoRouteFilter, CategoryFilter]
    #     elif 'geo_point' in self.request.query_params:
    #         filter_backends = [GeoPointFilter, CategoryFilter]

    #     for backend in list(filter_backends):
    #         queryset = backend().filter_queryset(self.request, queryset, view=self)

    #     return queryset

    # def get_serializer_class(self):
    #     if self.request.user.is_staff:
    #         return FullAccountSerializer
    #     return BasicAccountSerializer