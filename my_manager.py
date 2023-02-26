import threading

class ProcessManager:
    def __init__(self):
        self.processes = []
        self.lock = threading.Lock()

    def start_process(self, target, args=()):
        p = threading.Thread(target=target, args=args)
        with self.lock:
            self.processes.append(p)
        p.start()

    def stop_process(self, target):
        with self.lock:
            for p in self.processes:
                if p.name == target.__name__:
                    p.stop()
                    self.processes.remove(p)
                    return True
        return False

    def get_processes(self):
        with self.lock:
            return [p.name for p in self.processes]
