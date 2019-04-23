# -*- coding:utf-8 -*- 
#进行数据库的初始化工作
from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy#要使用flask封装的sqlachemy
from sqlalchemy import Column, Integer, String


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield#这里将执行传入的操作
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

db = SQLAlchemy()  # 实例化,用来映射到数据库中,要和核心对象app绑定起来,现在是实例化自己的sqlachemy
# 定义一个基类
class Base(db.Model):#这样使子模型直接继承此base就行
    __abstract__=True#默认会直接创建这个表，但是我们不希望创建
    create_time=Column('create_time',Integer)
    def __init__(self):
        self.create_time=int(datetime.now().timestamp())#模型生成的时间

    def set_attrs(self,attrs_dict):
        for key,value in attrs_dict.item():
            #判断key在模型中是否有对应属性
            if hasattr(self,key) and key!='id':#判断当前对象是否有名字叫key的属性
                setattr(self,key,value)#对当前对象名字叫key的属性赋值value
        pass
