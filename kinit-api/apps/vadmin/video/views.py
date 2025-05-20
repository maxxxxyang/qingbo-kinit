#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2025/05/20 12:51
# @File           : views.py
# @IDE            : PyCharm
# @desc           : 路由，视图文件

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from . import models, schemas, crud, params
from core.dependencies import IdList
from apps.vadmin.auth.utils.current import AllUserAuth
from utils.response import SuccessResponse
from apps.vadmin.auth.utils.validation.auth import Auth
from core.database import db_getter


app = APIRouter()


###########################################################
#    视频稿件管理
###########################################################
@app.get("/article", summary="获取视频稿件列表", tags=["视频稿件管理"])
async def get_video_article_fw_list(p: params.VideoArticleFwParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.VideoArticleFwDal(auth.db).get_datas(**p.dict())
    return SuccessResponse(datas, count=count)


@app.post("/article", summary="创建视频稿件", tags=["视频稿件管理"])
async def create_video_article_fw(data: schemas.VideoArticleFw, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.VideoArticleFwDal(auth.db).create_data(data=data))


@app.delete("/article", summary="删除视频稿件", description="硬删除", tags=["视频稿件管理"])
async def delete_video_article_fw_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.VideoArticleFwDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/article/{data_id}", summary="更新视频稿件", tags=["视频稿件管理"])
async def put_video_article_fw(data_id: int, data: schemas.VideoArticleFw, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.VideoArticleFwDal(auth.db).put_data(data_id, data))


@app.get("/article/{data_id}", summary="获取视频稿件信息", tags=["视频稿件管理"])
async def get_video_article_fw(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.VideoArticleFwSimpleOut
    return SuccessResponse(await crud.VideoArticleFwDal(db).get_data(data_id))

