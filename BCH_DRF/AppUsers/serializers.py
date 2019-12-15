from django.utils import timezone

from rest_framework import serializers

from CoreApp.models import User, ProfilePics

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    password            = serializers.CharField(label='Password', write_only=True)
    password2           = serializers.CharField(label='Confirm Password', write_only=True)

    class Meta:
        model           = User
        fields          = ( 'id', 
                            'url', 
                            'email', 
                            'username',
                            'password', 
                            'password2', 
                            'is_owner', )

    def validate(self, data):
        pass1           = data.get('password')
        pass2           = data.get('password2')
        if pass1 != pass2:
            raise serializers.ValidationError('Both passwords must match')
        return data

    def create(self, validated_data):
        user_obj        = User(
            username    = validated_data.get('username'),
            email       = validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active = False
        user_obj.save()
        return user_obj


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    joined_since         = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model           = User
        fields          = ( 'id',
                            'url',
                            'email', 
                            'username',
                            'first_name', 
                            'last_name', 
                            'image', 
                            'joined_since', 
                            'password',
                            'is_owner',
                            'is_staff', )
        extra_kwargs    = {
            'is_staff'  : {  'read_only':True,},
            'is_owner'  : {  'read_only':True,},
            'email'     : {  'read_only':True,},
            'password'  : {  'write_only':True,
                             'style':{'input_style':'password'}} }

    def update(self, instance, validated_data):
        instance.username=(validated_data.get('username'))
        instance.first_name=(validated_data.get('first_name'))
        instance.last_name=(validated_data.get('last_name'))
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def get_joined_since(self, obj):
        return (timezone.now() - obj.timestamp).days


class UserDetailAdminSerializer(UserDetailSerializer):
    
    class Meta:
        model           = User
        fields          = ( 'id',
                            'url', 
                            'email', 
                            'username', 
                            'first_name', 
                            'last_name', 
                            'image', 
                            'joined_since',
                            'is_owner', 
                            'is_staff', 
                            'is_active', 
                            'is_superuser')
        extra_kwargs    = {
            'password'  : {  'write_only':True,
                             'style':{'input_style':'password'}}}


class UserDetailStaffSerializer(UserDetailSerializer):
    
    class Meta:
        model           = User
        fields          = ( 'id', 
                            'url',
                            'email', 
                            'username', 
                            'first_name', 
                            'last_name', 
                            'joined_since',
                            'is_owner', 
                            'is_staff', 
                            'is_active')
        extra_kwargs    = {
            'password'  : {  'write_only':True,
                             'style':{'input_style':'password'}}}

class UserListSerializer(UserDetailSerializer):
    class Meta:
        model           = User
        fields          = ( 'url',
                            'username', 
                            'image')


class UserInfoSerializer(UserDetailSerializer):

    class Meta:
        model           = User
        fields          = ( 'username', 
                            'email')
