#!/usr/bin/env sh

set +e

if [ -z ${CRON_SCHEDULE+x} ]; then
  /usr/local/bin/backup
else
  CRON_SCHEDULE=${CRON_SCHEDULE}
  echo "${CRON_SCHEDULE} python /usr/local/bin/py/connect.py" > /etc/crontabs/root
  # Starting cron
  crond -f -d 0
fi