#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2025/05/20 12:51
# @File           : crud.py
# @IDE            : PyCharm
# @desc           : 数据访问层

from sqlalchemy import select, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import DalBase
from . import models, schemas
from .schemas import VideoArticleFwSimpleOut
from datetime import datetime


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

    async def get_datas(self, page: int = 1, limit: int = 10, v_order_field: str = None, v_order: str = None, articletype: str = None, title: str = None, **kwargs):
        sql = select(self.model).where(self.model.deleted_at == None)
        # 新增筛选条件
        if articletype:
            sql = sql.where(self.model.articletype == articletype)
        if title:
            sql = sql.where(self.model.title.like(f"%{title}%"))
        # 排序
        if v_order_field and hasattr(self.model, v_order_field):
            order_col = getattr(self.model, v_order_field)
            if v_order == 'desc':
                sql = sql.order_by(order_col.desc())
            elif v_order == 'asc':
                sql = sql.order_by(order_col.asc())
        else:
            sql = sql.order_by(self.model.id.desc())
        # 统计总数
        count_sql = select(func.count()).select_from(self.model).where(self.model.deleted_at == None)
        if articletype:
            count_sql = count_sql.where(self.model.articletype == articletype)
        if title:
            count_sql = count_sql.where(self.model.title.like(f"%{title}%"))
        total = (await self.db.execute(count_sql)).scalar()
        # 分页
        sql = sql.offset((page - 1) * limit).limit(limit)
        result = await self.db.execute(sql)
        datas = result.scalars().all()
        result_list = []
        for i in datas:
            item = VideoArticleFwSimpleOut.model_validate(i).model_dump()
            if item.get('publishTime'):
                if isinstance(item['publishTime'], datetime):
                    item['publishTime'] = item['publishTime'].strftime('%Y-%m-%d %H:%M:%S')
                else:
                    try:
                        item['publishTime'] = datetime.fromisoformat(str(item['publishTime'])).strftime('%Y-%m-%d %H:%M:%S')
                    except Exception:
                        pass
            result_list.append(item)
        return result_list, total

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
