#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2025/05/20 12:51
# @File           : crud.py
# @IDE            : PyCharm
# @desc           : 数据访问层

from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import DalBase
from . import models, schemas


class VideoArticleFwDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(VideoArticleFwDal, self).__init__()
        self.db = db
        self.model = models.VideoArticleFw
        self.schema = schemas.VideoArticleFwSimpleOut
