from datetime import datetime, timedelta
import json
import math

def open_file(path):
	with open(path) as f:
		return [i.strip() for i in f.readlines()]

def convert_datetime_to_string(d, d_format):
	return d.strftime(d_format)

def convert_string_to_datetime(d, d_format):
	return datetime.strptime(d, d_format)

def write_csv_data(file_path, data):
    with open(file_path, 'a') as f:
        writer = csv.writer(f)
        f.write(data)

def write_json_data(file_path, data):
	with open(file_path, 'w') as f:
		f.write(json.dumps(data, indent=4))

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def roundup(x):
	return int(math.ceil(x / 100.0)) * 100