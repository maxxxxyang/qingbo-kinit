#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2025/05/20 12:51
# @File           : video_article_fw.py
# @IDE            : PyCharm
# @desc           : 稿件相似度

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class VideoArticleFwParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
