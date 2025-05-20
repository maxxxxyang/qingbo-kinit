from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from core.database import Base
import datetime

class VideoArticleFW(Base):
    __tablename__ = 'video_article_fw'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')
    title = Column(String(255), nullable=False, comment='稿件标题')
    video_url = Column(String(1024), nullable=False, comment='视频地址')
    cover_url = Column(String(1024), comment='封面图片地址')
    author = Column(String(64), comment='作者')
    description = Column(Text, comment='视频描述')
    status = Column(Integer, default=1, comment='状态 1-正常 0-禁用')
    is_deleted = Column(Boolean, default=False, comment='是否删除')
    create_time = Column(DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间') 