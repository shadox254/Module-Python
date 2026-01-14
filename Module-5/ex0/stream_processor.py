from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass


    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, list):
                raise ValueError
        except:
            print("Validation: Error, data is not a list")
            return False
        try:
            if len(data) == 0:
                raise ValueError
        except ValueError:
            print("Validation: Error, data cannot be empty")
            return False
        for number in data:
            try:
                int(number)
            except (ValueError, TypeError):
                print("Validation: Error, data is not a list containing only numeric values.")
                return False
        print("Validation: Numeric data verified")
        return True

    def process(self, data: Any) -> str:
        total_sum = sum(number for number in data)
        data_len = len(data)
        average = total_sum/data_len
        text = f"Processed {data_len} numeric values, sum={total_sum}, avg={average}"
        return text


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        else:
            print("Validation: Error, data is not a string")
            return False

    def process(self, data: Any) -> str:
        data_len = len(data)
        count_word = len(data.split())
        text = f"Processed text: {data_len} characters, {count_word} words"
        return text


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            print("Validation: Error, data is not a string")
            return False
        if not ":" in data:
            print("Validation: Error, missing \":\" to indicate the type of error")
            return False
        print("Validation: Log entry verified")
        return True

    def process(self, data: Any) -> str:
        text = ""
        error_flag = data.split(":", 1)
        if "ERROR" in error_flag:
            text += "[ALERT] "
        elif "INFO" in error_flag:
            text += "[INFO] "
        elif "WARNING" in error_flag:
            text += "[WARNING] "
        else:
            text += "[UNKNOW] "
        text += error_flag[0] + " level detected:"
        return text + error_flag[1]


def stream_processor():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    print("Initializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    validate = numeric_processor.validate(data)
    if validate == True:
        print(numeric_processor.format_output(numeric_processor.process(data)))
    print()

    print("Initializing Text Processor...")
    data = "Hello Nexus World"
    print(f"Processing data: \"{data}\"")
    validate = text_processor.validate(data)
    if validate == True:
        print(text_processor.format_output(text_processor.process(data)))
    print()

    print("Initializing Log Processor...")
    data = "ERROR: Connection timeout"
    print(f"Processing data: \"{data}\"")
    validate = log_processor.validate(data)
    if validate == True:
        print(log_processor.format_output(log_processor.process(data)))
    print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    
    data = [
        (numeric_processor, [1, 2, 3]),
        (text_processor, "Hello World!"),
        (log_processor, "INFO: System ready")
    ]

    i = 0
    for processor, data in data:
        print(f"Result {i + 1}: {processor.process(data)}")
        i += 1
    print()

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
