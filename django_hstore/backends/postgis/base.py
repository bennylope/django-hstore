import logging

from django_hstore.backends.postgis.creation import PostGISCreation

from ..postgresql_psycopg2.base import HstoreCreationMixin, DatabaseWrapper

log = logging.getLogger(__name__)


class DatabaseCreation(HstoreCreationMixin, PostGISCreation):
    pass
