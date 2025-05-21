#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2025/05/20 12:51
# @File           : video_article_fw.py
# @IDE            : PyCharm
# @desc           : 稿件相似度

from fastapi import Depends, Query
from core.dependencies import Paging, QueryParams


class VideoArticleFwParams(QueryParams):
    def __init__(self, articletype: str = Query(None), title: str = Query(None), params: Paging = Depends()):
        super().__init__(params)
        self.articletype = articletype
        self.title = title
