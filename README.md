# HowTo

1. Open /data/data/me.webalert/databases (with Cx Datei Explorer: Enable root folder access before)
2. Backup webchecker.sql (wal and shm files too)
3. Delete webchecker.sql 
4. Start Webalert
5. Check webchecker.sql was created
6. Close Webalert
7. Copy webchecker.sql to /Downloads (with Cx Datei Explorer)
8. Execute run.py file (In case of ddl changes: adapt models.py and delete webtracker.db before executing script)
9. Open webtracker.db in VirtualBox (Program "DB Browser for SQLite")
10. Export table jobs (Datei - Export - Datenbank zu SQL Datei) with option "Nur Daten exportieren"
11. Open empty webchecker.sql database
12. Import exported jobs table (do not replace existing database)
13. Write changes
14. Copy webchecker.sql to /data/data/me.webalert/databases
15. Start Webalert
16. Enjoy
