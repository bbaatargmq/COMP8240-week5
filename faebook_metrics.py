
import csv
import argparse

def facebook_metrics(filename):
    
    data_total_reach = {}
    data_total_count = {}

    with open("dataset_Facebook.csv", "r") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader, None)
    
        for row in reader:
            post_type = row[1]
            reach = int(row[7])
                
            if post_type in data_total_count:
                data_total_reach[post_type] += reach
                data_total_count[post_type] += 1
            else:
                data_total_reach[post_type] = reach
                data_total_count[post_type] = 1
                
    with open("facebook_statistics.csv", "w") as f:
    
        csv_writter = csv.writer(f)
        csv_writter.writerow(["Type", "Total", "Count", "Mean"])
    
    
        for post_type in data_total_reach:
                
            mean = data_total_reach[post_type] / data_total_count[post_type]
            print("Type", post_type)
            print("Total", data_total_count[post_type])
            print("Count", data_total_count[post_type])
            print("Mean", mean)
            
            csv_writter.writerow([post_type, data_total_reach[post_type], data_total_count[post_type], mean])    
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Facebook metrics")
    parser.add_argument("filename", help="Input CSV file (dataset_Facebook.csv)")
    args = parser.parse_args()

    facebook_metrics(args.filename)