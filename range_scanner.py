#!/usr/bin/env python3
"""Simple TCP port-range scanner (Day 49 — Port Scanning & Reconnaissance).

Attempts a TCP connect() to every port in a range on one target and reports
which ones respond. This is the same technique behind a basic "connect scan",
without any stealth or evasion features.

Only scan hosts and networks you own or are explicitly authorized to test.
Scanning systems without permission may be illegal.

Usage:
    python range_scanner.py <target> <start_port> <end_port>
    python range_scanner.py                # prompts for the same values

Example:
    python range_scanner.py 127.0.0.1 20 1024
"""

import argparse
import socket
import sys
from datetime import datetime

MIN_PORT = 0
MAX_PORT = 65535


def scan_port_range(target: str, start_port: int, end_port: int) -> None:
    """Scan `target` from `start_port` to `end_port` (inclusive) and print open ports."""
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


def parse_port(value: str, name: str) -> int:
    try:
        port = int(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer, got {value!r}") from exc
    if not (MIN_PORT <= port <= MAX_PORT):
        raise ValueError(f"{name} must be between {MIN_PORT} and {MAX_PORT}, got {port}")
    return port


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="range_scanner",
        description="Scan a target for open TCP ports in a given range.",
    )
    parser.add_argument("target", nargs="?", help="IP address or hostname to scan")
    parser.add_argument("start_port", nargs="?", help=f"first port to scan ({MIN_PORT}-{MAX_PORT})")
    parser.add_argument("end_port", nargs="?", help=f"last port to scan ({MIN_PORT}-{MAX_PORT})")
    return parser


def main(argv=None) -> int:
    args = build_arg_parser().parse_args(argv)

    target = args.target or input("Enter target IP or hostname: ").strip()
    start_raw = args.start_port if args.start_port is not None else input("Enter start port: ").strip()
    end_raw = args.end_port if args.end_port is not None else input("Enter end port: ").strip()

    if not target:
        print("[-] Target must not be empty.", file=sys.stderr)
        return 1

    try:
        start = parse_port(start_raw, "start_port")
        end = parse_port(end_raw, "end_port")
    except ValueError as exc:
        print(f"[-] {exc}", file=sys.stderr)
        return 1

    if start > end:
        print("[-] Invalid port range: start_port must not be greater than end_port.", file=sys.stderr)
        return 1

    scan_port_range(target, start, end)
    return 0


if __name__ == "__main__":
    sys.exit(main())
