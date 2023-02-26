import multiprocessing as mp

class MultiProcessManager:
    def __init__(self):
        self.processes = []
        self.results = mp.Manager().list()
        
    def start_process(self, target, args=()):
        process = mp.Process(target=target, args=args)
        process.start()
        self.processes.append(process)
        
    def stop_process(self, index):
        if self.processes[index].is_alive():
            self.processes[index].terminate()
        del self.processes[index]
        
    def stop_all_processes(self):
        for process in self.processes:
            if process.is_alive():
                process.terminate()
        self.processes = []
        
    def get_results(self):
        return list(self.results)
        
    def append_result(self, result):
        self.results.append(result)




















