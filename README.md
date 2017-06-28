# ZabbixMySQL
Zabbix MySQL Monitoring Scripts and Templates

Pumps SHOW GLOBAL VARIABLES; and SHOW GLOBAL STATUS; to Zabbix via zabbix_sender
Call this with an item on your Zabbix server or midserver with system.run[mysql_sender.sh] or put it in externalscripts and call with external check.
