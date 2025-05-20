"""add video_article_fw table

Revision ID: 9cda4eca939f
Revises: 8d9867a5de90
Create Date: 2025-05-20 09:45:49.681777

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9cda4eca939f'
down_revision = '8d9867a5de90'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'video_article_fw',
        sa.Column('id', sa.BigInteger(), primary_key=True, autoincrement=True, comment='稿件ID'),
        sa.Column('articleID', sa.String(100), nullable=True, comment='标题相似值（相等表示标题相似）'),
        sa.Column('sameid', sa.String(100), nullable=True, comment='正文相似值（相等表示正文相似）'),
        sa.Column('sameid3', sa.String(100), nullable=True, comment='正文相似值（相等表示正文相似）'),
        sa.Column('articletype', sa.String(255), nullable=True, comment='稿件类型'),
        sa.Column('title', sa.String(255), nullable=True, comment='稿件标题'),
        sa.Column('publishTime', sa.DateTime(), nullable=True, comment='发布时间'),
        sa.Column('url', sa.String(255), nullable=True, comment='原网url'),
        sa.Column('dataSourceID', sa.Integer(), nullable=False, comment='数据源ID'),
        sa.Column('dataSourceName', sa.String(255), nullable=True, comment='数据源名称'),
        sa.Column('mediaID', sa.Integer(), nullable=False, comment='媒体ID'),
        sa.Column('mediaName', sa.String(255), nullable=True, comment='媒体名称'),
        sa.Column('keywords', sa.String(255), nullable=True, comment='关键词'),
        sa.Column('readcount', sa.Integer(), nullable=False, server_default='0', comment='阅读量'),
        sa.Column('agreecount', sa.Integer(), nullable=False, server_default='0', comment='点赞量'),
        sa.Column('forwardcount', sa.Integer(), nullable=False, server_default='0', comment='转发量'),
        sa.Column('commentcount', sa.Integer(), nullable=False, server_default='0', comment='评论量'),
        sa.Column('collectcount', sa.Integer(), nullable=False, server_default='0', comment='收藏量'),
        sa.Column('watchcount', sa.Integer(), nullable=False, server_default='0', comment='在看量'),
        sa.Column('degree', sa.Integer(), nullable=False, server_default='0', comment='热度'),
        sa.Column('video_article_id', sa.Integer(), nullable=False, server_default='0', comment='视频关联id'),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True, comment='创建时间'),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True, comment='更新时间'),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True, comment='删除时间'),
        mysql_engine='InnoDB',
        mysql_charset='utf8mb4'
    )
    op.create_unique_constraint('uniq_articleID', 'video_article_fw', ['articleID'])


def downgrade():
    op.drop_table('video_article_fw')
