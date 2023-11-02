# Create a dump from AWS RDS: (This doesn't include the users)
### pg_dump
```bash
$ pg_dump -h <HOST> -U <USERNAME> -f dump.sql -d <SOURCE_DATABASE_TO_CONNECT>
```

### Load pg_dump into local database: 
* https://hevodata.com/learn/postgresql-dump-import/-:~:text=Postgres%20Import%20Dump%20process%20can,file%20with%20the%20psql%20tool.
```bash
$ psql -U <USERNAME> -d <DABASE_NAME_AT_TARGET> -f dump.sql
```



# pg_dumpall: Create Users/Roles
* https://www.postgresql.org/docs/current/app-pg-dumpall.html
* `--globals-only` to dump only objects(roles and tablespaces), no databases
* `--roles-only` to dump only roles, no databases or tablespaces.
* Example of exporting only roles/users:
```bash
$ pg_dumpall --roles-only --no-role-passwords -h <HOST> -U <USERNAME> -f <OUTPUT_FILE>
```


# Steps to dump/recreate a database with the users (Have to set the user passwords afterward)
1) Dump the database with pg_dump: `pg_dump -h <HOST> -U <USERNAME> -f dump.sql -d <DATABASE_TO_CONNECT>`
2) Create a new DB on the target database:
 * `$ su - postgres`
 * `$ psql`
 * `CREATE DATABASE <DABASE_NAME_AT_TARGET>;`
3) Create a dump file with the roles/users with pg_dumpall: `$ pg_dumpall --roles-only --no-role-passwords -h <HOST> -U <USERNAME> -f <OUTPUT_FILE>`
4) Load users/roles from pg_dumpall file: `$ psql -U <USERNAME> -d <DABASE_NAME_AT_TARGET> -f <dump_filename>`
5) Load schemas/tables/grants from pg_dump file: `$ psql -U <USERNAME> -d <DABASE_NAME_AT_TARGET> -f <dump_filename>`
6) Change passwords of users with: `ALTER USER <USERNAME> WITH PASSWORD '<PWD>';`
Done! All schemas/tables were created on database `DABASE_NAME_AT_TARGET` with all users with correct grants!
