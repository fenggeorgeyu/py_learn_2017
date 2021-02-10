all:

run_test_connect:
	python3 test_connect.py

run_test_create_db:
	python3 test_create_db.py

export_json:
	sqlite3 -header -json test.db "select * from company;" > company.json

export_cvs:
	sqlite3 -header -csv test.db "select * from company;" > company.csv