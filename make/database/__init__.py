from make.command import BaseCommand

import os

from subprocess import call


class DBCommand(BaseCommand):
    name = 'db'
    description = 'DB inicialization, synchronization and migration tools.'

    def createsuperuser(self):
        call('sudo -iu postgres psql -d template1 -c "CREATE USER rootb WITH PASSWORD \'test\';"', shell=True)
        call('sudo -i -u postgres psql -d template1 -c "ALTER USER rootb WITH SUPERUSER;"', shell=True)

    def init(self):
        os.environ['PGPASSWORD'] = 'test'
        call('psql -U rootb -d template1 -c "SELECT pid, pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid <> pg_backend_pid() AND datname = \'testdb\';"', shell=True, env=os.environ)
        call('psql -U rootb -d template1 -c "DROP DATABASE IF EXISTS testdb;"', shell=True, env=os.environ)
        call('psql -U rootb -d template1 -c "DROP USER IF EXISTS testusr;"', shell=True, env=os.environ)
        call('psql -U rootb -d template1 -c "CREATE DATABASE testdb;"', shell=True, env=os.environ)
        call('psql -U rootb -d template1 -c "CREATE USER testusr WITH PASSWORD \'testpasswd\';"', shell=True, env=os.environ)
        call('psql -U rootb -d template1 -c "GRANT ALL PRIVILEGES ON DATABASE testdb TO testusr;"', shell=True, env=os.environ)

    def handle(self, *args, **kwargs):
        getattr(self, args[0])()

