#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2025/05/20 12:51
# @File           : crud.py
# @IDE            : PyCharm
# @desc           : 数据访问层

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import DalBase
from . import models, schemas
from .schemas import VideoArticleFwSimpleOut


class VideoArticleFwDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(VideoArticleFwDal, self).__init__()
        self.db = db
        self.model = models.VideoArticleFw
        self.schema = schemas.VideoArticleFwSimpleOut

    async def get_data(self, data_id: int = None, **kwargs):
        sql = select(self.model).where(self.model.deleted_at == None)
        if data_id is not None:
            sql = sql.where(self.model.id == data_id)
        result = await self.db.execute(sql)
        data = result.scalar_one_or_none()
        if data:
            return VideoArticleFwSimpleOut.model_validate(data).model_dump()
        return None

    async def get_datas(self, page: int = 1, limit: int = 10, **kwargs):
        sql = select(self.model).where(self.model.deleted_at == None)
        sql = sql.offset((page - 1) * limit).limit(limit)
        result = await self.db.execute(sql)
        datas = result.scalars().all()
        count = len(datas)
        return [VideoArticleFwSimpleOut.model_validate(i).model_dump() for i in datas], count

    async def delete_datas(self, ids: list[int], v_soft: bool = False, **kwargs) -> None:
        if v_soft:
            await self.db.execute(
                update(self.model).where(self.model.id.in_(ids)).values(
                    deleted_at=None,
                    **kwargs
                )
            )
        else:
            await self.db.execute(delete(self.model).where(self.model.id.in_(ids)))
        await self.db.flush()

    async def put_data(self, data_id: int, data: schemas.VideoArticleFw, **kwargs):
        obj = await self.get_data(data_id)
        obj_dict = data.dict(exclude_unset=True)
        for key, value in obj_dict.items():
            setattr(obj, key, value)
        await self.db.flush(obj)
        return obj
