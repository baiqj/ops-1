#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by 'Administrator' on '2014/12/13'
import web
from config import URLS, site_config, urls_config


app = web.application(URLS, globals())
web.config.debug = site_config.debug

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'),  {'user': None})
    web.config._session = session
else:
    session = web.config._session

web.template.Template.globals.update({'urls_config': urls_config, 'session': session})


if __name__ == '__main__':
    app.run()