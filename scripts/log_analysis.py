import os  # For file operations
import re  # For regular expressions
import csv  # For writing CSV files
from collections import Counter  # For counting IP addresses and endpoints
import argparse  # For command-line arguments


def count_requests_per_ip(log_file):
    """
    Counts the number of requests per IP address from the log file.
    
    Args:
        log_file (str): Path to the log file.

    Returns:
        list: A list of tuples containing IP addresses and their request counts.
    """
    ip_counter = Counter()
    try:
        with open(log_file, 'r') as file:
            for line in file:
                try:
                    ip = line.split()[0]  # Extract IP address
                    ip_counter[ip] += 1
                except IndexError:
                    print(f"Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file {log_file} does not exist.")
        return []
    except Exception as e:
        print(f"Unexpected error while processing IPs: {e}")
        return []
    return ip_counter.most_common()


def most_frequent_endpoint(log_file):
    """
    Finds the most frequently accessed endpoint from the log file.
    
    Args:
        log_file (str): Path to the log file.

    Returns:
        tuple: A tuple containing the most accessed endpoint and its count.
    """
    endpoint_counter = Counter()
    try:
        with open(log_file, 'r') as file:
            for line in file:
                endpoint_match = re.search(r'\"(?:GET|POST|PUT|DELETE) (.*?) HTTP', line)
                if endpoint_match:
                    endpoint = endpoint_match.group(1)
                    endpoint_counter[endpoint] += 1
    except FileNotFoundError:
        print(f"Error: The file {log_file} does not exist.")
        return ("N/A", 0)
    except Exception as e:
        print(f"Unexpected error while processing endpoints: {e}")
        return ("N/A", 0)
    return endpoint_counter.most_common(1)[0] if endpoint_counter else ("N/A", 0)


def detect_suspicious_activity(log_file, threshold=10):
    """
    Detects suspicious activity based on failed login attempts exceeding a threshold.
    
    Args:
        log_file (str): Path to the log file.
        threshold (int): The threshold for failed login attempts.

    Returns:
        list: A list of tuples containing IP addresses and their failed login counts.
    """
    failed_login_counter = Counter()
    try:
        with open(log_file, 'r') as file:
            for line in file:
                try:
                    if '401' in line or 'Invalid credentials' in line:
                        ip = line.split()[0]
                        failed_login_counter[ip] += 1
                except IndexError:
                    print(f"Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file {log_file} does not exist.")
        return []
    except Exception as e:
        print(f"Unexpected error while processing suspicious activity: {e}")
        return []
    suspicious_ips = [(ip, count) for ip, count in failed_login_counter.items() if count > threshold]
    return suspicious_ips


def save_results_to_csv(ip_requests, most_frequent, suspicious_activities, output_file):
    """
    Saves the analysis results to a CSV file.

    Args:
        ip_requests (list): List of tuples with IP addresses and request counts.
        most_frequent (tuple): Most accessed endpoint and its count.
        suspicious_activities (list): List of tuples with IP addresses and failed login counts.
        output_file (str): Path to the output CSV file.
    """
    try:
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Requests per IP
            writer.writerow(["Requests per IP"])
            writer.writerow(["IP Address", "Request Count"])
            writer.writerows(ip_requests)
            writer.writerow([])

            # Most Accessed Endpoint
            writer.writerow(["Most Accessed Endpoint"])
            writer.writerow(["Endpoint", "Access Count"])
            writer.writerow(most_frequent)
            writer.writerow([])

            # Suspicious Activity
            writer.writerow(["Suspicious Activity"])
            writer.writerow(["IP Address", "Failed Login Count"])
            writer.writerows(suspicious_activities)

    except PermissionError:
        print(f"Error: Permission denied when writing to {output_file}. Check file permissions.")
    except Exception as e:
        print(f"Error while saving to CSV: {e}")


def display_results(ip_requests, most_frequent, suspicious_activities):
    """
    Displays the analysis results in the terminal.

    Args:
        ip_requests (list): List of tuples with IP addresses and request counts.
        most_frequent (tuple): Most accessed endpoint and its count.
        suspicious_activities (list): List of tuples with IP addresses and failed login counts.
    """
    # Display IP requests
    print("\nRequests per IP:")
    print("IP Address           Request Count")
    for ip, count in ip_requests:
        print(f"{ip:20}{count}")

    # Display Most Frequent Endpoint
    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_frequent[0]} (Accessed {most_frequent[1]} times)")

    # Display Suspicious Activity
    if suspicious_activities:
        print("\nSuspicious Activity Detected:")
        print("IP Address           Failed Login Attempts")
        for ip, count in suspicious_activities:
            print(f"{ip:20}{count}")
    else:
        print("\nNo suspicious activity detected.\n")


# Main function for argument parsing and execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Log Analysis Script')
    parser.add_argument('--log_file', type=str, default=r'D:\Job_Intern_Projects\Log Analysis Script assignment\vrv_log_analysis\data\sample.log', help='Path to the log file.')
    parser.add_argument('--output_file', type=str, default=r'D:\Job_Intern_Projects\Log Analysis Script assignment\vrv_log_analysis\results\log_analysis_results.csv', help='Path to the output CSV file.')
    parser.add_argument('--threshold', type=int, default=10, help='Failed login attempt threshold.')

    args = parser.parse_args()

    ip_requests = count_requests_per_ip(args.log_file)
    most_frequent = most_frequent_endpoint(args.log_file)
    suspicious_activities = detect_suspicious_activity(args.log_file, args.threshold)

    # Display results in terminal
    display_results(ip_requests, most_frequent, suspicious_activities)

    # Save results to CSV
    save_results_to_csv(ip_requests, most_frequent, suspicious_activities, args.output_file)
