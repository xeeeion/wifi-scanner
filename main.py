import tkinter as tk
from tkinter import ttk
import pywifi

class WifiScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wi-Fi Scanner")
        self.create_widgets()

    def create_widgets(self):
        self.scan_button = ttk.Button(self.root, text="Scan Wi-Fi", command=self.scan_wifi)
        self.scan_button.pack(pady=10)

        self.results_label = tk.Label(self.root, text="Scan results will be shown here:", height=5)
        self.results_label.pack()

        self.results_text = tk.Text(self.root, height=50, width=100)
        self.results_text.pack()

    def scan_wifi(self):
        self.results_text.delete("1.0", tk.END)
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]

        iface.scan()
        scan_results = iface.scan_results()

        if scan_results:
            self.results_text.insert(tk.END, "Wi-Fi networks found:\n")
            for network in scan_results:
                ssid = network.ssid
                signal_strength = network.signal
                encryption_type = self.get_encryption_type(network)
                self.results_text.insert(tk.END,
                                         f"SSID: {ssid}, Signal Strength: {signal_strength} dBm, Encryption: "
                                         f"{encryption_type}\n")
        else:
            self.results_text.insert(tk.END, "No Wi-Fi networks found.")

    def get_encryption_type(self, network):
        akm = network.akm[0]
        if akm == 0:
            return "Open"
        elif akm == 1:
            return "WEP"
        elif akm == 2:
            return "WPA-PSK"
        elif akm == 3:
            return "WPA-EAP"
        elif akm == 4:
            return "WPA2-PSK"
        elif akm == 5:
            return "WPA2-EAP"
        elif akm == 6:
            return "WPA2/WPA3-SAE"
        elif akm == 8:
            return "WPA3-SAE"
        else:
            return f"Unknown ({akm})"

root = tk.Tk()
app = WifiScannerApp(root)
root.mainloop()
