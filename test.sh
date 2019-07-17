#!/usr/bin/env bash

NEW_DBNAME="AAA"
sql="SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid <> pg_backend_pid() AND datname = ${NEW_DBNAME};"
echo $sql

