# 学习笔记

* 1.查看django版本
    * django-admin --version
* 2.创建应用程序
    * python3.8 manage.py startapp index
* 3.url path匹配规则从上到下
* 4.使用pymysql报错
```
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.

修改：/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/django/db/backends/mysql/base.py
注释下面两行代码：
#if version < (1, 3, 13):
#    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

```

* 5.AttributeError: 'str' object has no attribute 'decode'
```
出现这个错误，打开/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/django/db/backends/mysql/operations.py文件，找到代码，注释判断查询为空的字符转码
    def last_executed_query(self, cursor, sql, params):
        # With MySQLdb, cursor objects have an (undocumented) "_executed"
        # attribute where the exact query sent to the database is saved.
        # See MySQLdb/cursors.py in the source distribution.
        query = getattr(cursor, '_executed', None)
       # if query is not None:
       #     query = query.decode(errors='replace')
        return query

```
* 6.通过ORM创建表
   * python3.8 manage.py makemigrations
   * python3.8 manage.py migrate