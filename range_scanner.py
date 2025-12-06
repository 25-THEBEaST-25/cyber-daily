import socket
from datetime import datetime

def scan_port_range(target: str, start_port: int, end_port: int) -> None:
    print(f"\n[+] Scanning {target} from port {start_port} to {end_port}")
    print(f"Started at: {datetime.now()}\n")

    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)  # half-second timeout

            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN]  Port {port}")
            s.close()

    except KeyboardInterrupt:
        print("\n[-] Scan stopped by user.")
    except socket.gaierror:
        print("[-] Hostname could not be resolved.")
    except socket.error:
        print("[-] Could not connect to server.")

    print(f"\nFinished at: {datetime.now()}")

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ").strip()
    start = int(input("Enter start port: ").strip())
    end = int(input("Enter end port: ").strip())

    if start < 0 or end > 65535 or start > end:
        print("[-] Invalid port range.")
    else:
        scan_port_range(target, start, end)
