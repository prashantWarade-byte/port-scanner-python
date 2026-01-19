import socket
from datetime import datetime

print("=== Simple Port Scanner ===")

target = input("Enter website or IP to scan: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print("\nScanning", target, "from port", start_port, "to", end_port)
print("-----------------------------------------")

start_time = datetime.now()

file = open("scan_report.txt", "w")
file.write("PORT SCAN REPORT\n")
file.write("Target: " + target + "\n")
file.write("Scan Time: " + str(start_time) + "\n\n")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    result = s.connect_ex((target, port))

    if result == 0:
        output = "Port " + str(port) + " is OPEN"
        print(output)
        file.write(output + "\n")

    s.close()

file.write("\nScan Completed.\n")
file.close()

print("\nScan Completed. Report saved as scan_report.txt")
