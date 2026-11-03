# Cognitive Event-Related Potential P300 Latency Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Event-Related Potential P300 Peak Latency (ms), Amplitude ($\mu\text{V}$), Age-Adjusted Latency Deviation, and Motor Processing Slack using oddball paradigm electrophysiology.

## Architecture

```mermaid
flowchart TD
    A[Oddball Paradigm Target Stimulus] --> B[Record Pz Scalp ERP Waveform]
    B --> C[Extract P300 Peak Latency ms & Amplitude uV]
    C --> D[Compute Age-Adjusted Predicted Latency & Deviation]
    D --> E[Calculate Motor Execution Slack RT - P300]
    E --> F[Classify Optimal Speed vs Cognitive Slowing]
```

## Quickstart

```python
from client import CognitiveP300LatencyClient

client = CognitiveP300LatencyClient()
result = client.evaluate_p300(
    p300_latency_ms=312.0,
    p300_amplitude_uv=14.5,
    patient_age_years=26,
    reaction_time_ms=370.0
)
print(result)
```

## License

Apache-2.0
