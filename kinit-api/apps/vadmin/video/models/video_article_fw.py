from core.database import Base
from sqlalchemy import BigInteger, String, Integer, DateTime, Column

class VideoArticleFw(Base):
    __tablename__ = 'video_article_fw'
    __table_args__ = {'extend_existing': True}
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='稿件ID')
    articleID = Column(String(100), nullable=True, comment='标题相似值（相等表示标题相似）')
    sameid = Column(String(100), nullable=True, comment='正文相似值（相等表示正文相似）')
    sameid3 = Column(String(100), nullable=True, comment='正文相似值（相等表示正文相似）')
    articletype = Column(String(255), nullable=True, comment='稿件类型')
    title = Column(String(255), nullable=True, comment='稿件标题')
    publishTime = Column(DateTime, nullable=True, comment='发布时间')
    url = Column(String(255), nullable=True, comment='原网url')
    dataSourceID = Column(Integer, nullable=False, comment='数据源ID')
    dataSourceName = Column(String(255), nullable=True, comment='数据源名称')
    mediaID = Column(Integer, nullable=False, comment='媒体ID')
    mediaName = Column(String(255), nullable=True, comment='媒体名称')
    keywords = Column(String(255), nullable=True, comment='关键词')
    readcount = Column(Integer, nullable=False, default=0, comment='阅读量')
    agreecount = Column(Integer, nullable=False, default=0, comment='点赞量')
    forwardcount = Column(Integer, nullable=False, default=0, comment='转发量')
    commentcount = Column(Integer, nullable=False, default=0, comment='评论量')
    collectcount = Column(Integer, nullable=False, default=0, comment='收藏量')
    watchcount = Column(Integer, nullable=False, default=0, comment='在看量')
    degree = Column(Integer, nullable=False, default=0, comment='热度')
    video_article_id = Column(Integer, nullable=False, default=0, comment='视频关联id')
    created_at = Column(DateTime, nullable=True, comment='创建时间')
    updated_at = Column(DateTime, nullable=True, comment='更新时间')
    deleted_at = Column(DateTime, nullable=True, comment='删除时间') 