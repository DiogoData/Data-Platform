import os
from datetime import datetime


class Ingestor:
    def __init__(self):
        self.connection = " "

    def save_to_bronze(self, data, file_format):
        day = datetime.now()
        with open(os.path.join(self.path, f"{day.strftime('%Y-%m-%d %H-%M-%S-%f')}.{file_format}"), "w") as f:
            f.write(data)

    def set_table(self, schema, table):
        date = datetime.now().strftime("%Y-%m-%d")
        self.path = f"./data/bronze/{schema}/{table}/{date}/"
        os.makedirs(self.path, exist_ok=True)