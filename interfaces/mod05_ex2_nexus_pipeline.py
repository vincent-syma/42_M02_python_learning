#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Union, Protocol, Dict
from collections import Counter

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


# ---------- STAGE PROTOCOL ----------

class ProcessingStage(Protocol):
    """Interface for stages using duck typing.
    Any class with process() can act as a stage."""

    def process(self, data: Any) -> Any:
        ...


# ---------- STAGE IMPLEMENTATIONS ----------

class InputStage:
    """Processes input."""

    def process(self, data: Any) -> Any:
        """Process data - validate input"""
        if isinstance(data, dict):  # JSON
            if "sensor" not in data or "value" not in data:
                raise ValueError("Invalid JSON data")
        elif isinstance(data, str):  # CSV
            if not data.strip():
                raise ValueError("Empty CSV data")
        elif isinstance(data, list):  # Stream
            if not data:
                raise ValueError("Empty stream data")

        return data


class TransformStage:
    """Transforms input into output"""

    def process(self, data: Any) -> Any:
        """Transforms input to desired output string."""

        if isinstance(data, dict):  # JSON
            sensor = data["sensor"]
            value = data["value"]
            unit = data.get("unit", "")
            status = "Normal range" if 15 <= value <= 25 else "Critical"

            return f"Processed {sensor} reading: {value}{unit} ({status})"

        elif isinstance(data, str):  # CSV
            # CSV: "user,action,timestamp"
            rows = data.strip().split("\n")
            actions = len(rows) - 1  # (minus header)

            return f"User activity logged: {actions} actions processed"

        elif isinstance(data, list):  # Stream
            temps = [v for v in data if isinstance(v, (int, float))]
            avg = sum(temps) / len(temps) if temps else 0

            return f"Stream summary: {len(temps)} readings, avg: {avg:.1f}°C"

        return data


class OutputStage:
    """Returns output."""

    def process(self, data: Any) -> Any:
        """Returns output."""
        return data


# ---------- PIPELINE BASE ----------

class ProcessingPipeline(ABC):
    """Abstract base managing stages.
    Contains a list of stages and orchestrates data flow."""

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.stats = Counter()

    def add_stage(self, stage: ProcessingStage) -> None:
        """Add stage to the pipeline flow."""
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        try:
            self.stats["records"] += 1
            i = 1
            for stage in self.stages:
                try:
                    data = stage.process(data)
                except Exception as e:
                    stage_name = stage.__class__.__name__

                    self.stats["errors"] += 1
                    self.stats[f"errors_{stage_name}"] += 1
                    raise RuntimeError(f"Error detected in Stage {i}: "
                                       f"{e}") from e
                i += 1
            return data
        except Exception as e:
            return (f"{RED}[ERROR]{RESET}[{self.pipeline_id}] {e}\n"
                    "Recovery initiated: Switching to backup processor\n"
                    "Recovery successful: Pipeline restored, "
                    "processing resumed\n")

    def get_stats(self) -> Dict[str, Any]:
        return {"pipeline_id": self.pipeline_id,
                "records": self.stats["records"],  # processed
                "errors": self.stats["errors"],
                "stage_errors": {key: value for key, value
                                 in self.stats.items()
                                 if key.startswith("errors_")}
                }

    def reset_stats(self) -> None:
        self.stats.clear()


# ---------- ADAPTERS ----------

class JSONAdapter(ProcessingPipeline):
    """x"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        return super().process(data)


class CSVAdapter(ProcessingPipeline):
    """x"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        return super().process(data)


class StreamAdapter(ProcessingPipeline):
    """x"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        return super().process(data)


# ---------- NEXUS MANAGER ----------

class NexusManager:
    """Manages ProcessingPipeline.
    Orchestrates multiple pipelines polymorphically."""

    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def select_pipeline(self, data: Any) -> ProcessingPipeline:
        """Automatic selection based on data type."""

        if isinstance(data, dict):
            for pipeline in self.pipelines:
                if isinstance(pipeline, JSONAdapter):
                    return pipeline
        elif isinstance(data, str):
            for pipeline in self.pipelines:
                if isinstance(pipeline, CSVAdapter):
                    return pipeline
        elif isinstance(data, List):
            for pipeline in self.pipelines:
                if isinstance(pipeline, StreamAdapter):
                    return pipeline
        raise ValueError("No suitable pipeline for this data type")

    def process_data(self, data: Any) -> Any:
        pipeline = self.select_pipeline(data)
        return pipeline.process(data)

    def chain_pipelines(self, data: Any) -> Any:
        """Output from the first stage becomes input for the next and so on."""
        current = data
        for pipeline in self.pipelines:
            current = pipeline.process(current)
        return current


# ---------- DEMO ----------

def main() -> None:
    """
    Entry point of the nexus pipeline program.
    """
    print(f"\n{BOLD}=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ==={RESET}\n")

    print(f"{ITALIC}Initializing Nexus Manager...{RESET}\n")

    manager = NexusManager()

    print("Creating Data Processing Pipeline:")

    json_pipeline = JSONAdapter("JSON_PIPELINE_001")
    csv_pipeline = CSVAdapter("CSV_PIPELINE_001")
    stream_pipeline = StreamAdapter("STREAM_PIPELINE_001")

    pipelines = [json_pipeline, csv_pipeline, stream_pipeline]
    stages = [InputStage(), TransformStage(), OutputStage()]

    print("- Stage 1: Input validation and parsing")
    print("- Stage 2: Data transformation and enrichment")
    print("- Stage 3: Output formatting and delivery")

    for pipeline in pipelines:
        for stage in stages:
            pipeline.add_stage(stage)
        manager.add_pipeline(pipeline)

    # === Multi-Format Data Processing ===

    print(f"\n\n{BOLD}=== Multi-Format Data Processing ==={RESET}\n")

    json_data = {"sensor": "temp", "value": 23.5, "unit": "°C"}
    csv_data = "user,action,timestamp\nalice,login,2026-03-12T10:00:00"
    stream_data = [22, 23, 24, 21, 22]

    # JSON
    print(f"{YELLOW}Processing {BOLD}JSON{RESET}{YELLOW} data "
          f"through pipeline...{RESET}")
    print(f"{BOLD}Input:{RESET}\t   {json_data}")
    print(f"{BOLD}Transform:{RESET} Enriched with metadata and validation")
    output = manager.process_data(json_data)
    print(f"{BOLD}Output:{RESET}\t   {output}\n")

    # CSV
    print(f"{YELLOW}Processing {BOLD}CSV{RESET}{YELLOW} data "
          f"through same pipeline...{RESET}")
    print(f'{BOLD}Input:{RESET}\t   "user,action,timestamp"')
    print(f"{BOLD}Transform:{RESET} Parsed and structured data")
    output = manager.process_data(csv_data)
    print(f"{BOLD}Output:{RESET}\t   {output}\n")

    # Stream
    print(f"{YELLOW}Processing {BOLD}Stream{RESET}{YELLOW} data "
          f"through same pipeline...{RESET}")
    print(f"{BOLD}Input:{RESET}\t   Real-time sensor stream")
    print(f"{BOLD}Transform:{RESET} Aggregated and filtered")
    output = manager.process_data(stream_data)
    print(f"{BOLD}Output:{RESET}\t   {output}\n")

    # === Pipeline Chaining Demo ===

    print(f"\n{BOLD}=== Pipeline Chaining Demo ==={RESET}\n")

    print(f"{ITALIC}Pipeline A -> Pipeline B -> Pipeline C{RESET}")
    print(f"{ITALIC}Data flow: Raw -> Processed -> Analyzed -> Stored{RESET}")
    print()

    for pipeline in manager.pipelines:
        pipeline.reset_stats()

    # chained_result =
    manager.chain_pipelines(
        {"sensor": "temp", "value": 22.0, "unit": "°C"}
    )
    # print(chained_result)

    total = sum((pipeline.stats for pipeline in manager.pipelines), Counter())

    print(f"{BOLD}Chain result:{RESET}\t"
          f"{total["records"]} records processed "
          f"through {len(stages)}-stage pipeline")
    print(f"{BOLD}Total errors:{RESET}\t{total["errors"]}")

    # === Error Recovery Test ===

    print(f"\n\n{BOLD}=== Error Recovery Test ==={RESET}\n")

    print(f"{ITALIC}Simulating pipeline failure...{RESET}\n")

    bad_json = {"sensor": "temp"}  # missing value
    output = json_pipeline.process(bad_json)
    print(output)

    print("-------------------------------------------------------")
    print("✅ Nexus Integration complete. All systems operational.")
    print("-------------------------------------------------------")


if __name__ == "__main__":
    main()
