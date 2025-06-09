import time

from flask import jsonify


class TimelineService:
    def stream_numbers(self):
        for number in range(5):
            time.sleep(1)
            data = {
                "loading": True,
                "data": "step one",
            }
            
            if number < 4:
                data["data"] = f"step {number + 1}"
                data["loading"] = True
                stringified_data = str(data)
                yield f'data: {stringified_data}\n\n'
            else:
                structured_response = {
                    "param_1": "value_1",
                    "param_2": "value_2",
                    "param_3": "value_3",
                }

                data["loading"] = False
                data["data"] = structured_response

                stringified_data = str(data)

                yield f'data: {stringified_data}\n\n'