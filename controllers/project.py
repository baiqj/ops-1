#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by 'Administrator' on '2014/12/13'
from config import render


class Index(object):
    def GET(self):
        return render.project.index('项目列表')