#https://chat.openai.com/share/fe2b803b-d26f-4339-aa5b-46bd0bd09ef6
import json, csv, re 
with open('regex\\u5l03-1-cw-error-logs-via-regex-kyuril\\logs.json') as file: 
    data = json.load(file)

    with open('error_logs.csv', 'w+', newline="") as newFile: 
        writer = csv.writer(newFile)
        header = ["timestamp", "level", "message"] 
        writer.writerow(header)


        pattern = r"ERROR"
        #write data into the csv file 
        for row in data:
            if re.search(pattern, row["level"], re.IGNORECASE):
                timestamp = row.get("timestamp")
                level = "ERROR"
                message = row.get("message")
                writer.writerow([timestamp, level, message])