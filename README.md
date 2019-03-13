# elk_backup_python
For elasticsearch 2.3.0
To use image should be identified variables like:

CRON_SCHEDULE: "*/2 * * * *" (may not be used, for 1 time backup)

es_host: "pa_elasticsearch"

indices: "index1,index2" (or * for all indexes)

repository_name: "elk_backup"

Backup volume should be mounted ONLY to /usr/share/elasticsearch/backups folder inside container
