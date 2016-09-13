#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO
from config import SQLALCHEMY_DATABASE_URL
api.upgrade(SQLALCHEMY_DATABASE_URL, SQLALCHEMY_MIGRATE_REPO)
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URL, SQLALCHEMY_MIGRATE_REPO))
