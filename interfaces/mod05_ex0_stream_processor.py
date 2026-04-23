#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Union

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


class DataProcessor(ABC):
    """
    Abstract base class defining the common processing interface.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process input data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate input data for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Default output formatting (can be overridden)."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized on numeric input."""

    def process(self, data: Any) -> str:
        """
        Process input data (List[Union[int, float]])
        and return a result string.
        """
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data "
                                 "(must be List[Union[int, float]])")

            numbers: List[Union[int, float]] = data
            total: float = sum(numbers)
            count: int = len(numbers)
            average: float = total / count if count > 0 else 0

            result: str = (
                f"Processed {count} numeric values, "
                f"sum={total}, avg={average}"
            )
            return result

        except Exception as e:
            return f"{RED}Numeric processing error:{RESET} {e}"

    def validate(self, data: Any) -> bool:
        """
        Validate input data for this processor:
        List[Union[int, float]].
        """
        if not isinstance(data, list):
            return False
        return all(isinstance(x, (int, float)) for x in data)


class TextProcessor(DataProcessor):
    """Processor specialized on text input."""

    def process(self, data: Any) -> str:
        """Process input data (str) and return a result string."""
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")

            text: str = data
            chars: int = len(text)
            words: int = len(text.split())

            result: str = (f"Processed text: {chars} characters, "
                           f"{words} words")
            return result

        except Exception as e:
            return f"{RED}Text processing error:{RESET} {e}"

    def validate(self, data: Any) -> bool:
        """Validate input data for this processor: str"""
        if not isinstance(data, str):
            return False
        return all(isinstance(x, str) for x in data)


class LogProcessor(DataProcessor):
    """Processor specialized on log input."""

    def process(self, data: Any) -> str:
        """
        Process input data (str - log syntax) and return a result string.
        (LOG_LEVEL: text)
        """
        try:
            if not self.validate(data):
                raise ValueError("Invalid log entry")

            log_entry: str = data

            if ":" not in log_entry:
                raise ValueError("Malformed log entry")

            level_part, message = log_entry.split(":", 1)
            level: str = level_part.strip().upper()
            message = message.strip()

            if level == "ERROR":
                prefix = f"{BOLD_RED}ALERT{RESET}"
            elif level == "INFO":
                prefix = "INFO"
            elif level == "WARNING":
                prefix = f"{RED}WARN{RESET}"
            else:
                prefix = "LOG"

            result: str = (f"[{prefix}] {level} level detected: {message}")
            return result

        except Exception as e:
            return f"{RED}Log processing error:{RESET} {e}"

    def validate(self, data: Any) -> bool:
        """Validate input data for this processor: str"""
        return isinstance(data, str)


def main() -> None:
    """
    Entry point of the stream processor program.
    """
    print()
    print(f"{BOLD}=== CODE NEXUS - DATA PROCESSOR FOUNDATION ==={RESET}")
    print()

    numeric = NumericProcessor()
    num_data: List = [1, 2, 3, 4, 5]
    print(f"Initializing {YELLOW}Numeric Processor{RESET}...")
    print(f"Processing data: {num_data}")
    if (numeric.validate(num_data)):
        print("Validation: Numeric data verified")
    print(numeric.format_output(numeric.process(num_data)))
    print()

    text = TextProcessor()
    text_data: str = "Hello Nexus World"
    print(f"Initializing {YELLOW}Text Processor{RESET}...")
    print(f"Processing data: {text_data}")
    if (text.validate(text_data)):
        print("Validation: Text data verified")
    print(text.format_output(text.process(text_data)))
    print()

    log = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    print(f"Initializing {YELLOW}Log Processor{RESET}...")
    print(f"Processing data: {log_data}")
    if (text.validate(log_data)):
        print("Validation: Log data verified")
    print(log.format_output(log.process(log_data)))
    print()

    print(f"{BOLD}=== Polymorphic Processing Demo ==={RESET}")
    print()

    print("Processing multiple data types through same interface...")
    print()

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    print("VALID DATA:")
    val_data_items = [
        [1, 2, 3],
        "42Nexus World",
        "INFO: System ready"
    ]

    count = 1
    for data in val_data_items:
        matched = False
        for processor in processors:
            if processor.validate(data):
                result = processor.process(data)
                print("Result:", result)
                count += 1
                matched = True
                break
        if not matched:
            print("Result: No suitable processor found for:", data)
    print()

    print("INVALID DATA:")
    inval_data_items = [
        [1, "a", 3],
        5,
        "42Nexus World"
    ]
    count = 1
    for processor, data in zip(processors, inval_data_items):
        result = processor.process(data)
        print(f"Result {count}:", result)
        count += 1
    print()
    print("✅ Foundation systems online. Nexus ready for advanced streams.")
    print()
    print("---------------------------------------------")


if __name__ == "__main__":
    main()
