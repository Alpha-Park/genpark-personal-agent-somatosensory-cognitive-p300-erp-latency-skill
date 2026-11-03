"""
Example usage of Cognitive P300 Latency & Attention Dynamics Skill.
Demonstrates normal youthful cognitive speed vs marked cognitive delay in neurodegenerative decline.
"""

import json
from client import CognitiveP300LatencyClient


def main():
    print("=== Testing Cognitive P300 Latency Skill ===")
    client = CognitiveP300LatencyClient()

    # 1. Healthy young adult subject (P300 latency = 312 ms, amp = 14.5 uV, RT = 370 ms, age = 26 -> Predicted = 307.5 ms, Normal)
    res_normal = client.evaluate_p300(
        p300_latency_ms=312.0,
        p300_amplitude_uv=14.5,
        patient_age_years=26,
        reaction_time_ms=370.0,
        electrode_site="Pz"
    )
    print("\n[Case 1: Normal Cognitive Processing Speed]")
    print(json.dumps(res_normal, indent=2))

    # 2. Patient with neurodegenerative cognitive impairment (P300 latency prolonged to 485 ms, amp attenuated to 3.2 uV, RT = 620 ms, age = 72)
    res_impaired = client.evaluate_p300(
        p300_latency_ms=485.0,
        p300_amplitude_uv=3.2,
        patient_age_years=72,
        reaction_time_ms=620.0,
        electrode_site="Pz"
    )
    print("\n[Case 2: Significant Neurocognitive Impairment]")
    print(json.dumps(res_impaired, indent=2))

    # Assertions
    assert res_normal["p300_measurements"]["p300_latency_ms"] < res_normal["normative_indices"]["upper_limit_normal_ms"]
    assert "Optimal" in res_normal["cognitive_assessment"]["cognitive_status"]
    assert res_impaired["p300_measurements"]["p300_latency_ms"] > 450.0
    assert "Significant" in res_impaired["cognitive_assessment"]["cognitive_status"]
    print("\n[SUCCESS] Cognitive P300 Latency tests passed!")


if __name__ == "__main__":
    main()
