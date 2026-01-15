from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, id: str) -> None:
        self.stream_id = id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        filtered_list = []
        for element in data_batch:
            if criteria in str(element):
                filtered_list.append(element)
        return filtered_list

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = {"event_id": self.stream_id, "type": self.stream_type}
        return stats


class SensorStream(DataStream):
    def __init__(self, id):
        super().__init__(id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch):
        text = ""
        process_count = len(data_batch)
        try:
            for element in data_batch:
                key, value = element.split(":")
                if key is None or value is None:
                    raise ValueError
        except ValueError:
            return "Error, the format of one of the elements in data_batch is invalid. Format: “element”:“value”"
        filtered_list = self.filter_data(data_batch, "temp")
        try:
            temp_sum = sum(float(element.split(":")[1]) for element in filtered_list)
        except ValueError:
            return "Error, one of the temperatures is not numeric"
        try:
            temp_count = len(filtered_list)
            if temp_count == 0:
                raise ValueError
        except ValueError:
            return "Error, data_batch does not contain temperature "
        print(f"Processing sensor batch: {data_batch}")
        average_temp = temp_sum / temp_count
        print("Sensor analysis: ", end="")
        text += f"{process_count} reading processed, avg temp: {average_temp}°C"
        return text


class TransactionStream(DataStream):
    def __init__(self, id):
        super().__init__(id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch):
        money = 0
        text = ""
        try:
            for element in data_batch:
                key, value = element.split(":")
                if key is None or value is None:
                    raise ValueError
        except ValueError:
            return "Error, the format of one of the elements in data_batch is invalid. Format: “element”:“value”"
        try:
            for element in data_batch:
                int(element.split(":")[1])
        except ValueError:
            return "Error, price value or sale value is not a number"
        try:
            for element in data_batch:
                operations = element.split(":")[0]
                if operations not in "buy sell":
                    raise ValueError
        except ValueError:
            return "Unknown operations, only “buy” and “sell” operations are available."
        print(f"Processing transaction batch: {data_batch}")
        print("Transaction analysis: ", end="")
        operations_count = len(data_batch)
        text += f"{operations_count} operations, net flow: "
        for operations in data_batch:
            op_type, value = operations.split(":")
            if op_type == "buy":
                money -= int(value)
            elif op_type == "sell":
                money += int(value)
        if money > 0:
            text += "+"
        text += f"{money} units"
        return text


class EventStream(DataStream):
    def __init__(self, id):
        super().__init__(id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch):
        text = ""
        try:
            event_count = len(data_batch)
            if event_count == 0:
                raise ValueError
        except ValueError:
            return "Error, data_batch cannot be empty"
        print(f"Processing event batch: {data_batch}")
        print("Event analysis: ", end="")
        error_count = len(self.filter_data(data_batch, "error"))
        if error_count == 1:
            text += f"{event_count} events, {error_count} error detected"
        elif error_count > 1:
            text += f"{event_count} events, {error_count} errors detected"
        elif error_count == 0:
            text += f"{event_count} events, no error detected"
        return text


def sensor_stream_process(data_batch: List[Any]):
    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    sensor_stats = sensor_stream.get_stats()
    try:
        print(f"Stream ID: {sensor_stats['event_id']}, Type: {sensor_stats['type']}")
    except KeyError:
        print("Error, one of the keys of sensor_stats is incorrect")
        return None
    print(sensor_stream.process_batch(data_batch))


def transaction_stream_process(data_batch: List[Any]):
    print("Initializing Transaction Stream...")
    transa_stream = TransactionStream("TRANS_001")
    transa_stats = transa_stream.get_stats()
    try:
        print(f"Stream ID: {transa_stats['event_id']}, Type: {transa_stats['type']}")
    except KeyError:
        print("Error, one of the keys of transa_stats is incorrect")
        return None
    print(transa_stream.process_batch(data_batch))


def event_stream_process(data_batch: List[Any]):
    print("Initializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    event_stats = event_stream.get_stats()
    try:
        print(f"Stream ID: {event_stats['event_id']}, Type: {event_stats['type']}")
    except KeyError:
        print("Error, one of the keys of event_stats is incorrect")
        return None
    print(event_stream.process_batch(data_batch))


def data_stream():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    data_batch = ["humidity:65", "pressure:1013"]
    sensor_stream_process(data_batch)
    print()

    # data_batch = ["buy:100", "sell:150", "buy:75"]
    # transaction_stream_process(data_batch)
    # print()

    # data_batch = ["login", "error", "logout"]
    # event_stream_process(data_batch)
    # print()

    # print("=== Polymorphic Stream Processing ===")
    # print("Processing mixed stream types through unified interface...")
    # print()

    # print("Batch 1 Results:")
    


if __name__ == "__main__":
    data_stream()
