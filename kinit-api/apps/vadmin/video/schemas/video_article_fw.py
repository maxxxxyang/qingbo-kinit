#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2025/05/20 12:51
# @File           : video_article_fw.py
# @IDE            : PyCharm
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class VideoArticleFw(BaseModel):
    articleID: str | None = Field(None, title="标题相似值（相等表示标题相似）")
    sameid: str | None = Field(None, title="正文相似值（相等表示正文相似）")
    sameid3: str | None = Field(None, title="正文相似值（相等表示正文相似）")
    articletype: str | None = Field(None, title="稿件类型")
    title: str | None = Field(None, title="稿件标题")
    publishTime: datetime | None = Field(None, title="发布时间")
    url: str | None = Field(None, title="原网url")
    dataSourceID: int = Field(..., title="数据源ID")
    dataSourceName: str | None = Field(None, title="数据源名称")
    mediaID: int = Field(..., title="媒体ID")
    mediaName: str | None = Field(None, title="媒体名称")
    keywords: str | None = Field(None, title="关键词")
    readcount: int = Field(0, title="阅读量")
    agreecount: int = Field(0, title="点赞量")
    forwardcount: int = Field(0, title="转发量")
    commentcount: int = Field(0, title="评论量")
    collectcount: int = Field(0, title="收藏量")
    watchcount: int = Field(0, title="在看量")
    degree: int = Field(0, title="热度")
    video_article_id: int = Field(0, title="视频关联id")
    created_at: datetime | None = Field(None, title="创建时间")
    updated_at: datetime | None = Field(None, title="更新时间")
    deleted_at: datetime | None = Field(None, title="删除时间")


class VideoArticleFwSimpleOut(VideoArticleFw):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., title="编号")
