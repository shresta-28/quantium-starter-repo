import csv
with open('data/daily_sales_data_0.csv') as data_file_0:
    csv_reader = csv.reader(data_file_0, delimiter=',')
    with open('clean_data.csv', mode='w') as writing_file:
        fieldnames = ['Sales', 'Date', 'Region']
        writer = csv.DictWriter(writing_file, fieldnames=fieldnames)        
        writer.writeheader()
        next(csv_reader)
        for row in csv_reader:
            if  row[0]=="pink morsel":
                price = float(row[1].replace('$', ''))
                quantity = int(row[2])
                writer.writerow({'Sales': price*quantity, 'Date': row[3], 'Region': row[4]})
with open('data/daily_sales_data_1.csv') as data_file_0:
    csv_reader = csv.reader(data_file_0, delimiter=',')
    with open('clean_data.csv', mode='a') as writing_file:
        fieldnames = ['Sales', 'Date', 'Region']
        writer = csv.DictWriter(writing_file, fieldnames=fieldnames)        
        next(csv_reader)
        for row in csv_reader:
            if  row[0]=="pink morsel":
                price = float(row[1].replace('$', ''))
                quantity = int(row[2])
                writer.writerow({'Sales': price*quantity, 'Date': row[3], 'Region': row[4]})
with open('data/daily_sales_data_2.csv') as data_file_0:
    csv_reader = csv.reader(data_file_0, delimiter=',')
    with open('clean_data.csv', mode='a') as writing_file:
        fieldnames = ['Sales', 'Date', 'Region']
        writer = csv.DictWriter(writing_file, fieldnames=fieldnames)        
        next(csv_reader)
        for row in csv_reader:
            if  row[0]=="pink morsel":
                price = float(row[1].replace('$', ''))
                quantity = int(row[2])
                writer.writerow({'Sales': price*quantity, 'Date': row[3], 'Region': row[4]})