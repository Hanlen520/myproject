# -*- coding:utf-8 -*-
from rest_framework import serializers
from myapp.serializers import Login


class Login1(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"
