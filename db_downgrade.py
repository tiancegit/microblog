#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URL
from config import SQLALCHEMY_MIGRATE_REPO
v = api.db_version(SQLALCHEMY_DATABASE_URL, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URL, SQLALCHEMY_MIGRATE_REPO, v-1)
