import psutil

class SystemMonitor:
    def __init__(self):
        self.processes = self.get_processes()
        self.cpu_usage = self.get_cpu_usage()
        self.network_io_counters = self.get_network_io_counters()
        self.sensors_temperatures = self.get_sensors_temperatures()
        self.usb_devices = self.get_usb_devices()
        self.ethernet_network = self.get_ethernet_network()
        self.functions = {
            'processes': self.get_processes,
            'cpu_usage': self.get_cpu_usage,
            'network_io_counters': self.get_network_io_counters,
            'sensors_temperatures': self.get_sensors_temperatures,
            'usb_devices': self.get_usb_devices,
            'ethernet_network': self.get_ethernet_network
        }

    def get_processes(self):
        return {p.pid: p.info for p in psutil.process_iter(['pid', 'name', 'username'])}

    def get_cpu_usage(self):
        return psutil.cpu_percent()

    def get_network_io_counters(self):
        return psutil.net_io_counters()

    def get_sensors_temperatures(self):
        return psutil.sensors_temperatures()

    def get_usb_devices(self):
        return [d.device for d in psutil.disk_partitions(all=True) if 'usb' in d.opts]

    def get_ethernet_network(self):
        return [nic for nic in psutil.net_if_stats().keys() if psutil.net_if_stats()[nic].isup]

    def get_function(self, function_name):
        return self.functions.get(function_name, lambda: None)()

    def get_all_functions(self):
        return {name: func() for name, func in self.functions.items()}
