from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, id: str) -> None:
        self.stream_id = id
        self.type = "Generic Stream"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        filtered_list = []
        for element in data_batch:
            if criteria in str(element):
                filtered_list.append(element)
        return filtered_list

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = {"id": self.stream_id, "type": self.type}
        return stats


class SensorStream(DataStream):
    def __init__(self, id):
        super().__init__(id)
        self.type = "Environmental Data"

    def process_batch(self, data_batch: List[Any] = None) -> str:
        if data_batch is None:
            raise ValueError("Error, data_batch cannot be None")
        if not isinstance(data_batch, List):
            raise ValueError("Error, data_batch must be a list")
        if len(data_batch) == 0:
            raise ValueError("No data found")
        operation_count = 0
        temp_sum = 0
        temp_count = 0
        for data in data_batch:
            if ":" not in data:
                return "All data is not in the correct format"
            try:
                key, value = data.split(":")
                temp = float(value)
                if key == "temp":
                    temp_sum += temp
                    temp_count += 1
            except ValueError:
                raise ValueError("Invalid temperature")
            operation_count += 1
        if temp_count == 0:
            return f"{operation_count} readings processed"
        avg_temp = temp_sum/temp_count
        return f"{operation_count} readings processed, avg temp {avg_temp}"


class TransactionStream(DataStream):
    def __init__(self, id):
        super().__init__(id)
        self.type = "Financial Data"

    def process_batch(self, data_batch: List[Any] = None) -> str:
        if data_batch is None:
            raise ValueError("Error, data_batch cannot be None")
        if not isinstance(data_batch, List):
            raise ValueError("data_batch must be a list")
        if len(data_batch) == 0:
            raise ValueError("No data found")
        operation_count = 0
        flow = 0
        for data in data_batch:
            if ":" not in data:
                return "All data is not in the correct format"
            try:
                key, value = data.split(":")
                if "buy" in key:
                    flow -= int(value)
                elif "sell" in key:
                    flow += int(value)
            except ValueError:
                raise ValueError("Invalid value")
            operation_count += 1
        sign = ""
        if flow > 0:
            sign = "+"
        return f"{operation_count} operations, net flow: {sign}{flow} units"


class EventStream(DataStream):
    def __init__(self, id):
        super().__init__(id)
        self.type = "Systems Events"

    def process_batch(self, data_batch: List[Any] = None) -> str:
        if data_batch is None:
            raise ValueError("Error, data_batch cannot be None")
        if not isinstance(data_batch, List):
            raise ValueError("data_batch must be a list")
        if len(data_batch) == 0:
            raise ValueError("No data found")
        event_count = 0
        error_count = 0
        for data in data_batch:
            if not isinstance(data, str):
                return "All data is not in the correct format"
            if "error" in data:
                error_count += 1
            event_count += 1
        return f"{event_count} events, {error_count} error detected"


class StreamProcessor():
    def __init__(self):
        self.stream_list = []

    def add_stream(self, stream: DataStream):
        self.stream_list.append(stream)

    def process_stream(self, global_batch: Dict[str, List[str]]):
        for stream in self.stream_list:
            stream_id = stream.stream_id
            if stream_id in global_batch:
                stream_data = global_batch[stream_id]
                try:
                    result = stream.process_batch(stream_data)
                    print(f"- {stream_id} data: {result}")
                except ValueError as e:
                    raise ValueError(f"- {stream_id} error: {e}")
            else:
                print(f"- {stream_id}: No data available in this batch")


def data_stream():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

# ========== Sensor_Stream ========== #
    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    stats = sensor_stream.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    data_batch = [
        "temp:22.5",
        "humidity:65",
        "pressure:1013"
        ]
    print(f"Processing sensor batch: {data_batch}")
    try:
        analysis = sensor_stream.process_batch(data_batch)
        print(f"Sensor analysis: {analysis}")
    except ValueError as e:
        print(e)
    print()

# ========== Transaction_Stream ========== #
    print("Initializing Transaction Stream...")
    transa_stream = TransactionStream("TRANS_001")
    stats = transa_stream.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    data_batch = [
        "buy:100",
        "sell:150",
        "buy:75"
    ]
    print(f"Processing transaction batch: {data_batch}")
    try:
        analysis = transa_stream.process_batch(data_batch)
        print(f"Transaction analysis: {analysis}")
    except ValueError as e:
        print(e)
    print()

# ========== Event_Stream ========== #
    print("Initializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    stats = event_stream.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    data_batch = [
        "login",
        "error",
        "logout"
    ]
    print(f"Processing event batch: {data_batch}")
    try:
        analysis = event_stream.process_batch(data_batch)
        print(f"Event analysis: {analysis}")
    except ValueError as e:
        print(e)
    print()

# ========== Polymorphic_Stream ========== #
    print("Processing mixed stream types through unified interface...")
    print()

    stream_processor = StreamProcessor()
    stream_processor.add_stream(sensor_stream)
    stream_processor.add_stream(transa_stream)
    stream_processor.add_stream(event_stream)
    data_batch = {
        "SENSOR_001": ["critical:1", "critical:1"],
        "TRANS_001": ["sell:100", "buy:74", "sell:49", "buy:75"],
        "EVENT_001": ["login", "error", "logout"]
    }
    print("Batch 1 Results:")
    try:
        stream_processor.process_stream(data_batch)
    except ValueError as e:
        print(e)
    print()

    print("Stream filtering active: High-priority data only")
    critical_sensor = sensor_stream.filter_data(data_batch['SENSOR_001'],
                                                "critical")
    large_transaction = transa_stream.filter_data(data_batch['TRANS_001'],
                                                  "100")
    print(f"Filtered results: {len(critical_sensor)} critical sensor alerts, \
{len(large_transaction)} large transaction")
    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
