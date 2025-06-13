import socket
import threading

# Function to scan a single port
def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout for connection attempt
            result = s.connect_ex((target, port))  # Attempt connection
            if result == 0:
                print(f"[+] Port {port} is open")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Main function
def port_scanner(target, start_port, end_port):
    print(f"Scanning {target} for open ports...\n")
    
    threads = []  # List to store threads
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()  # Start thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("\nScanning complete!")

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    port_scanner(target_ip, start_port, end_port)


    















    

