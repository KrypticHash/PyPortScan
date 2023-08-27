# PyPortScan: Python Port Scanner 🕵️‍♂️

Welcome to PyPortScan, your go-to tool for network reconnaissance and security assessment! PyPortScan is a powerful and customizable Python-based port scanning utility designed to help you discover open ports on target hosts swiftly and efficiently. Whether you're a security enthusiast, network administrator, or curious coder, PyPortScan provides a user-friendly interface and rich functionality to aid in analyzing the connectivity landscape of your network.

## 🚀 Key Features:

- Fast and reliable port scanning using a variety of scanning techniques.
- Customizable scan ranges to target specific ports or entire port ranges.
- Multi-threaded execution for enhanced speed and efficiency.
- Support for common protocols such as TCP and UDP.
- Detailed scan reports with status and service information.
- User-friendly command-line interface for easy interaction.
- Open-source and extensible, inviting collaboration and contributions.

## 🔒 Use Cases:

- Network security audits to identify potential vulnerabilities.
- Monitoring and hardening network perimeters.
- Verifying firewall rules and network configurations.
- Investigating server/service availability and health.

## 📖 How to Use:

### Installation

1. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/KrypticHash/PyPortScan.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd PyPortScan
   ```

### Usage

1. Open a terminal window and navigate to the directory where the script is located.

2. Run the script using the following command:

   ```bash
   python PyPortScan.py
   ```

3. The script will prompt you to enter the target(s) you want to scan. You can input a single target or multiple targets separated by commas.

4. Next, you'll be asked to specify the number of ports you want to scan.

5. The script will then start scanning the specified ports on the provided target(s).

### Code Explanation

The `port_scanner.py` script consists of the following functions:

- `scan(target, ports)`: This function initiates the port scanning process. It iterates through the range of ports and calls the `scan_port` function for each port.

- `scan_port(ipaddress, port)`: This function attempts to establish a connection to the given IP address and port using a socket. If the connection is successful, it prints that the port is open. If there's an exception (connection error), it's caught and the port is considered closed.

The main part of the script takes user input for the target and the number of ports to scan. If multiple targets are specified, the script splits them by commas and scans each target individually.

### Examples

1. Scanning a single target:

   ```
   [*] Enter Target To Scan: 192.168.1.1
   [*] Enter How Many Ports You Want To Scan: 100
   ```

2. Scanning multiple targets:

   ```
   [*] Enter Target To Scan(Split Them By Comma (,)): 192.168.1.1, 10.0.0.2
   [*] Enter How Many Ports You Want To Scan: 50
   ```

### Disclaimer

This script is for educational and informational purposes only. Unauthorized scanning of systems without proper authorization is illegal and unethical. Ensure you have the necessary permissions before using this script on any target system.
