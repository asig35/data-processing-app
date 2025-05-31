#!/bin/bash
echo "Running database queries..."
sqlite3 instance/people.db ".mode column" ".headers on" ".read database_queries.sql" 