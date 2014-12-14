#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by 'Administrator' on '2014/12/13'
import web


site_config = web.storage(
    template_dir='templates',
    template_base='layout',
    static_dir='static',
    debug=True,
    template_cache=False,
)

urls_config = web.storage(
    # 前台
    frontend_index='/',

    # 账户
    accounts_user_list='/accounts/user/list',  # 列出用户
    accounts_user_add='/accounts/user/add',  # 添加用户
    accounts_user_delete='/accounts/user/delete',  # 删除用户
    accounts_user_profile='/accounts/user/profile',  # 用户信息
    accounts_signin='/accounts/signin',  # 登陆
    accounts_signout='/accounts/signout',  # 退出

    # 服务器
    servers_prefix='/servers',

    # 服务
    services_prefix='/services',

    # 项目
    projects_list='/projects/list',  # 列表项目
    projects_stage='/projects/stage',  # 环境

    # API
    api_prefix='/api/v1',
)

URLS = (
    urls_config.frontend_index, 'controllers.frontend.Index',
    urls_config.frontend_index+'/index', 'controllers.frontend.Index',

    urls_config.projects_list, 'controllers.project.Index',

)

render = web.template.render(site_config.template_dir, cache=site_config.template_cache, base=site_config.template_base)
db = web.database(dbn='mysql', db='ops', user='root', pw='xinhua3206')
