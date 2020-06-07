from amb.src.connection.db_management import base
from sqlalchemy import Column, Integer, ForeignKey, Table


association_table = Table(
    "association",
    base.metadata,
    Column("playlist_id", Integer, ForeignKey("playlist.id")),
    Column("track_id", Integer, ForeignKey("track.id")),
)
