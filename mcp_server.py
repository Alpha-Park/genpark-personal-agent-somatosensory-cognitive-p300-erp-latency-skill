"""
MCP Server for Cognitive P300 Latency & Attention Dynamics Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import CognitiveP300LatencyClient


def main():
    client = CognitiveP300LatencyClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_p300",
                            "description": "Calculates Event-Related Potential P300 Peak Latency (ms), P300 Amplitude (uV), Age-Adjusted Latency Deviation, and Motor Processing Slack using oddball paradigm electrophysiology.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "p300_latency_ms": {
                                        "type": "number",
                                        "description": "P300 positive peak latency in milliseconds (ms)."
                                    },
                                    "p300_amplitude_uv": {
                                        "type": "number",
                                        "description": "P300 waveform amplitude in microvolts (uV)."
                                    },
                                    "patient_age_years": {
                                        "type": "integer",
                                        "description": "Subject age in years (optional)."
                                    },
                                    "reaction_time_ms": {
                                        "type": "number",
                                        "description": "Behavioral motor reaction time in ms (optional)."
                                    },
                                    "electrode_site": {
                                        "type": "string",
                                        "description": "Scalp recording montage electrode site (default: Pz)."
                                    }
                                },
                                "required": [
                                    "p300_latency_ms",
                                    "p300_amplitude_uv"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_p300":
                try:
                    out = client.evaluate_p300(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
