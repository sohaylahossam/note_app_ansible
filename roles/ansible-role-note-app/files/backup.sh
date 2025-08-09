#!/bin/bash
TIMESTAMP=$(date +"%F_%T")
cp /opt/note_app/notes.db /backup/notes_db_$TIMESTAMP.sqlite
