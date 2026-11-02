def show_ont_info():
    print("\n" + "=" * 45)
    print("       FIBERHOME ONT INFORMATION")
    print("=" * 45)

    model = input("ONT Model       : ").strip()
    serial = input("Serial Number   : ").strip()
    mac = input("MAC Address     : ").strip()
    firmware = input("Firmware        : ").strip()

    print("\n[+] ONT DEVICE SUMMARY")
    print("-" * 45)
    print(f"Model           : {model or 'Not provided'}")
    print(f"Serial Number   : {serial or 'Not provided'}")
    print(f"MAC Address     : {mac or 'Not provided'}")
    print(f"Firmware        : {firmware or 'Not provided'}")
    print("-" * 45)
    print("[INFO] Data entered manually.")
