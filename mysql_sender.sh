#!/bin/bash
DB=$1
QUERY=$2
ZABBIX_HOST="127.0.0.1"
python check_mysql_bulk.py $DB -q $QUERY | grep -v ft_boolean_syntax | zabbix_sender -s $DB -z ${ZABBIX_HOST}  --input-file -
