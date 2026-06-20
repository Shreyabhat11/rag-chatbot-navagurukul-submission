import time

class Evaluator:

    def __init__(self):
        self.latencies = []

    def record_latency(self, latency):
        self.latencies.append(latency)

    def avg_latency(self):
        if not self.latencies:
            return 0

        return sum(self.latencies) / len(self.latencies)

    def p95_latency(self):

        if not self.latencies:
            return 0

        sorted_values = sorted(self.latencies)

        idx = int(
            len(sorted_values) * 0.95
        )

        return sorted_values[idx]