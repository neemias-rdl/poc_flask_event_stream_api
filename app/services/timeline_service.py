import time


class TimelineService:
    def stream_numbers(self):
        """
        Yields a stream of numbers (placeholder logic).
        """
        for number in range(1, 101):
            time.sleep(1)
            yield f"data: Message {number}\n\n"