# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: sqlOprate.py
@creatTime: 2019/08/08
"""

import pymssql
from pymysql import *
from Logs.log import get_log


class MySql:
    """
    function：封装成数据库操作方法增、删、改、查
    :return 返回增、删、改、查的结果
    """

    def __init__(self, host, port, db_name, user, passwd, charset='utf8'):
        """
        function:初始化数据库并连接
        :param host: 数据库主机地址
        :param port: 端口
        :param db_name: 数据库名词
        :param user: 数据库登录用户
        :param passwd: 数据库登录密码
        :param charset: 数据库字符集
        """
        self.log = get_log("MySql")
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db_name = db_name
        self.charset = charset
        self.log.info("开始连接数据库%s..." % self.host)
        self.conn = connect(host=self.host,
                            port=self.port,
                            user=self.user,
                            passwd=self.passwd,
                            db=self.db_name,
                            charset=self.charset)
        self.cur = self.conn.cursor()
        self.log.info("连接数据库{}成功,库名%s！".format(self.host, self.db_name))

    def insert_change_sql(self, sql):
        """
        function：数据库查询数据
        :param sql: 数据库执行语句
        :return:result 返回执行结果
        """
        try:
            result = self.cur.execute(sql)  # 执行数据库语句
            self.log.info(sql)
            self.conn.commit()  # 提交数据库语句
            self.log.info(result)
            return result
        except Exception as e:
            self.log.error(e)
            print(e)

    def query_sql(self, sql):
        """
        function：数据库查询数据
        :param sql: 数据库执行语句
        :return: data 以列表返回查询数据
        """
        try:
            self.cur.execute(sql)  # 执行数据库语句
            self.log.info(sql)
            data = self.cur.fetchall()  # 获取查询结果
            return data
        except Exception as e:
            self.log.error(e)
            print(e)

    def close_sql(self):
        self.conn.close()
        self.cur.close()
        self.log.info("关闭数据库{}连接,库名{}".format(self.host, self.db_name))


class MySqlServer:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.log = get_log("MySqlServer")
        self.log.info("开始连接数据库%s..." % self.host)
        self.conn = pymssql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    database=self.database)
        self.cur = self.conn.cursor()
        self.log.info("连接数据库{}成功,库名为{}！".format(self.host, self.database))

    def insert_change_sql(self, sql):
        """
        function：数据库查询数据
        :param sql: 数据库执行语句
        :return:result 返回执行结果
        """
        try:
            self.cur.execute(sql)  # 执行数据库语句
            self.log.info("执行数据库语句为：" + sql)
            self.conn.commit()  # 提交数据库语句
        except Exception as e:
            self.log.error(e)

    def query_sql(self, sql):
        """
        function：数据库查询数据
        :param sql: 数据库执行语句
        :return: data 以列表返回查询数据
        """
        try:
            self.cur.execute(sql)  # 执行数据库语句
            self.log.info("查询语句为：" + sql)
            data = self.cur.fetchall()  # 获取查询结果
            return data
        except Exception as e:
            self.log.error(e)
            print(e)

    def close_sql(self):
        self.conn.close()
        self.cur.close()
        self.log.info("关闭数据库{}连接,库名{}".format(self.host, self.database))
