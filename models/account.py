#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by 'Administrator' on '2014/12/13'
from config import db
from passlib.hash import pbkdf2_sha512


def get_user_by_id(id_):
    var = {'id_': id_}
    user = db.select('user', var, where='id=$id_', limit=1)[0]
    return user


def get_user_by_email(email):
    var = {'email': email}
    user = db.select('user', var, where='email=$email', limit=1)[0]
    return user


def get_user_by_username(username):
    var = {'username': username}
    user = db.select('user', var, where='username=$username', limit=1)[0]
    return user


def create_user(username, password, email, gender=0, nickname=None, **kwargs):
    password = pbkdf2_sha512.encrypt(password)
    last_id = db.insert('user', username=username, password=password)