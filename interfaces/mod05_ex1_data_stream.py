#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict, Optional

# ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

# combinations
BOLD_RED = BOLD + RED
BOLD_GREEN = BOLD + GREEN
BOLD_BLUE = BOLD + BLUE


class DataStream(ABC):
    """An abstract base class with core streaming functionality"""

    stream_type = "Base"

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.data_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        pass

    @abstractmethod
    def validate_batch(self, data_batch: List[Any]) -> bool:
        """Validate input data for this processor."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Default - Filter data based on criteria"""

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Default stream statistics"""

        return {"stream_id": self.stream_id,
                "stream_type": self.stream_type,
                "processed_count": self.data_count}

    def format_output(self, criteria: Optional[str] = None) -> str:
        """Default output formatting (can be overridden)."""

        stats = self.get_stats()
        count = stats['processed_count']

        if criteria:
            if count == 1:
                return f"Results: 1 {criteria} item found"
            return f"Results: {count} {criteria} items found"

        if count == 1:
            return "Data: 1 item processed"

        return f"Data: {count} items processed"


class SensorStream(DataStream):
    """Processes environmental data from sensors"""

    stream_type = "Environmental Data"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def validate_batch(self, data_batch: List[Any]) -> bool:
        """Validate input data for this processor."""

        for data in data_batch:
            if not isinstance(data, str):
                return False

            if ":" not in data:
                return False

            key, value = self.parse_entry(data)

            if key not in ["temp", "humidity", "pressure"]:
                return False

            try:
                float(value)
            except ValueError:
                return False

        return True

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data from sensors"""
        try:
            if not self.validate_batch(data_batch):
                raise ValueError("Invalid input data")

            temps = []
            self.data_count = 0

            for data in data_batch:
                key, value = self.parse_entry(data)
                self.data_count += 1

                if key == "temp":
                    temps.append(float(value))

            avg_temp = sum(temps) / len(temps) if temps else 0
            return (f"Sensor analysis: {self.data_count} readings processed, "
                    f"avg temp: {avg_temp}")

        except Exception as e:
            return f"{RED}SensorStream error:{RESET} {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Is able to filter:
        - high or low temperatures ("high_temp"/"low_temp")
        - both together ("critical")
        """
        parsed: tuple = [(data, *self.parse_entry(data))
                         for data in data_batch]

        if criteria == "high_temp":
            return [data for data, key, value in parsed
                    if key == "temp" and float(value) > 25]
        if criteria == "low_temp":
            return [data for data, key, value in parsed
                    if key == "temp" and float(value) < 15]
        if criteria == "critical":
            return [data for data, key, value in parsed
                    if key == "temp" and (float(value) > 25
                                          or float(value) < 15)]
        return data_batch

    def format_output(self, criteria: Optional[str] = None) -> str:
        stats = self.get_stats()
        count = stats['processed_count']
        if criteria:
            if count == 1:
                return f"Results: 1 {criteria} sensor alert"
            return f"Results: {count} {criteria} sensor alerts"
        if count == 1:
            return "Sensor data: 1 reading processed"
        return f"Sensor data: {count} readings processed"

    def parse_entry(self, data: str) -> tuple[str, str]:
        """Split 'key:value'."""

        key, value = data.split(":", 1)
        return key, value


class TransactionStream(DataStream):
    """Processes financial transactions data"""

    stream_type = "Financial Data"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def validate_batch(self, data_batch: List[Any]) -> bool:
        """Validate input data for this processor."""

        for data in data_batch:
            if not isinstance(data, str):
                return False

            if ":" not in data:
                return False

            key, value = self.parse_entry(data)

            if key not in ["buy", "sell"]:
                return False

            try:
                int(value)
            except ValueError:
                return False

        return True

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not self.validate_batch(data_batch):
                raise ValueError("Invalid input data")
            # ("Wrong syntax. Use 'buy:amount' or sell:'amount'")

            amounts = []
            self.data_count = 0

            for data in data_batch:
                key, value = self.parse_entry(data)
                amount = int(value)
                if key == "buy":
                    pass
                elif key == "sell":
                    amount = -amount

                self.data_count += 1
                amounts.append(amount)

            net_flow = sum(amounts)
            if net_flow > 0:
                return (f"Transaction analysis: {self.data_count} operations, "
                        f"net flow: +{net_flow} units")
            else:
                return (f"Transaction analysis: {self.data_count} operations, "
                        f"net flow: {net_flow} units")

        except Exception as e:
            return f"{RED}TransactionStream error:{RESET} {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Is able to filter transactions
        - according to their type ("buy"/"sell")
        - or big amount ("large")
        """

        parsed: tuple = [(data, *self.parse_entry(data))
                         for data in data_batch]

        if criteria in ("buy", "sell"):
            return [data for data, key in parsed
                    if key == criteria]
        if criteria == "large":
            return [data for data, _, value in parsed
                    if int(value) > 100]
        return data_batch

    def format_output(self, criteria: Optional[str] = None) -> str:
        stats = self.get_stats()
        count = stats['processed_count']

        if criteria:
            if count == 1:
                return f"Results: 1 {criteria} transaction"
            return f"Results: {count} {criteria} transactions"

        if count == 1:
            return "Transaction data: 1 operation processed"

        return f"Transaction data: {count} operations processed"

    def parse_entry(self, data: str) -> tuple[str, str]:
        """Split 'key:value'."""

        key, value = data.split(":", 1)
        return key, value


class EventStream(DataStream):
    """Processes event data"""

    stream_type = "System events"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.error_count: int = 0

    def validate_batch(self, data_batch: List[Any]) -> bool:
        """Validate input data for this processor."""
        for data in data_batch:
            if not isinstance(data, str):
                return False
        return True

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not self.validate_batch(data_batch):
                raise ValueError("Invalid input data")

            self.data_count = len(data_batch)
            self.error_count = sum(1 for data in data_batch
                                   if isinstance(data, str)
                                   and data.lower() == "error")

            stats = self.get_stats()
            events = stats["processed_count"]
            errors = stats["errors"]

            if errors == 1:
                return f"Event analysis: {events} events, 1 error detected"
            return f"Event analysis: {events} events, {errors} errors detected"

        except Exception as e:
            return f"{RED}EventStream error:{RESET} {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Event stream statistics"""
        stats = super().get_stats()
        stats["errors"] = self.error_count
        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Is able to filter error events ("error")."""

        if criteria == "error":
            return [data for data in data_batch if data.lower() == criteria]

        return data_batch

    def format_output(self, criteria: Optional[str] = None) -> str:
        stats = self.get_stats()
        count = stats['processed_count']

        if criteria:
            if count == 1:
                return f"Results: 1 {criteria} event"
            return f"Results: {count} {criteria} events"

        if count == 1:
            return "Event data: 1 event processed"
        return f"Event data: {count} events processed"


class StreamProcessor:
    """
    Processes batches of data by using multiple data streams of one interface.
    """
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams: List[DataStream] = streams

    def process_all(self, batches: List[tuple]) -> None:
        """
        Process multiple batches polymorphically,
        including selected filter
        """

        for batch, criteria in batches:
            matched = False

            for stream in self.streams:
                if stream.validate_batch(batch):
                    filtered = stream.filter_data(batch, criteria)
                    stream.process_batch(filtered)
                    print(f"- {stream.format_output(criteria)}")
                    matched = True
                    break

            if not matched:
                raise ValueError("No suitable stream found "
                                 f"for data batch: {batch}")


def main() -> None:
    """
    Entry point of the data stream program.
    """
    print()
    print(f"{BOLD}=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ==={RESET}")
    print()

    sensor = SensorStream("SENSOR_001")
    print(f"Initializing {YELLOW}Sensor Stream{RESET}...")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    stats = sensor.get_stats()
    print(f"Stream ID: {sensor.stream_id}, Type: {stats['stream_type']}")
    print("Processing sensor batch:", sensor_batch)
    print(sensor.process_batch(sensor_batch))
    print()

    transaction = TransactionStream("TRANS_001")
    print(f"Initializing {YELLOW}Transaction Stream{RESET}...")
    trans_batch = ['buy:100', 'sell:150', 'buy:75']
    stats = transaction.get_stats()
    print(f"Stream ID: {transaction.stream_id}, Type: {stats['stream_type']}")
    print(f"Processing batch: {trans_batch}")
    print(transaction.process_batch(trans_batch))
    print()

    event = EventStream("EVENT_001")
    print(f"Initializing {YELLOW}Event Stream{RESET}...")
    event_batch = ["login", "error", "logout"]
    stats = event.get_stats()
    print(f"Stream ID: {event.stream_id}, Type: {stats['stream_type']}")
    print("Processing batch:", event_batch)
    print(event.process_batch(event_batch))
    print()

    print("=== Polymorphic Stream Processing ===")
    print(f"{ITALIC}Processing mixed stream types "
          f"through unified interface...{RESET}")
    print()

    streams = [sensor, transaction, event]

    print("Batch 1 Results:")
    mixed_batches = [
        (["temp:30.7", "temp:12.4"], None),
        (['buy:100', 'sell:150', 'buy:75', 'sell:10'], None),
        (["login", "error", "logout"], None)
    ]
    processor = StreamProcessor(streams)
    processor.process_all(mixed_batches)
    print()

    print("Stream filtering active: High-priority data only")
    mixed_batches_filters = [
        (["temp:30.7", "temp:12.4"], "critical"),
        (['buy:100', 'sell:150', 'buy:75', 'sell:10'], "large"),
        (["login", "error", "logout"], "error")
    ]
    processor = StreamProcessor(streams)
    processor.process_all(mixed_batches_filters)
    print()
    print("✅ All streams processed successfully. Nexus throughput optimal.")
    print()
    print("---------------------------------------------")


if __name__ == "__main__":
    main()
