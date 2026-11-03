"""
Cognitive Event-Related Potential P300 Latency & Attention Dynamics Client.
Zero-mock pure Python standard library implementation.
Calculates P300 Peak Latency (ms), P300 Amplitude (uV), Age-Adjusted Latency Deviation,
and Motor Processing Slack via oddball paradigm neurophysiology.
"""

import math
from typing import Dict, Any, Optional


class CognitiveP300LatencyClient:
    """
    Evaluates neurocognitive processing speed, attentional allocation, and memory updating via ERP P300:
    - Oddball paradigm: 80% standard vs 20% target stimulus
    - P300 latency (ms): neural stimulus evaluation time
    - P300 amplitude (uV): attentional resources allocated to target
    - Predicted latency: 300.0 + 1.25 * (age - 20)
    - Motor execution slack: reaction_time_ms - p300_latency_ms
    """

    def __init__(self):
        pass

    def evaluate_p300(
        self,
        p300_latency_ms: float,
        p300_amplitude_uv: float,
        patient_age_years: Optional[int] = 30,
        reaction_time_ms: Optional[float] = None,
        electrode_site: Optional[str] = "Pz"
    ) -> Dict[str, Any]:
        """
        Calculates P300 cognitive speed parameters.
        p300_latency_ms: time from stimulus onset to peak positive P300 waveform (250 to 600 ms).
        p300_amplitude_uv: peak-to-peak or baseline-to-peak amplitude in microvolts (1.0 to 30.0 uV).
        patient_age_years: subject age in years.
        reaction_time_ms: motor button press reaction time in milliseconds (optional).
        electrode_site: scalp recording location (default Pz).
        """
        if p300_latency_ms <= 0 or p300_amplitude_uv < 0:
            raise ValueError("P300 latency and amplitude must be positive.")

        age = patient_age_years if patient_age_years and patient_age_years >= 18 else 25

        # Age-adjusted normal predicted latency:
        # P300 latency prolongs at approximately 1.25 ms per year of age after 20
        predicted_latency_ms = 300.0 + max(0.0, 1.25 * (age - 20.0))
        latency_deviation_ms = p300_latency_ms - predicted_latency_ms

        # Upper limit of normal (ULN ~ predicted + 35 ms, ~2 standard deviations)
        upper_limit_normal_ms = predicted_latency_ms + 35.0

        # Motor processing slack (ms): RT minus P300 latency
        motor_slack_ms = None
        if reaction_time_ms is not None:
            motor_slack_ms = round(reaction_time_ms - p300_latency_ms, 1)

        # Neurocognitive classification:
        # Latency <= ULN and Amplitude >= 7.0 uV: Normal cognitive processing speed
        # Latency > ULN or Amplitude 4.0 - 7.0 uV: Mild attentional / cognitive slowing
        # Latency > 450 ms or Amplitude < 4.0 uV: Significant cognitive impairment / neurodegenerative decline
        if p300_latency_ms > 450.0 or p300_amplitude_uv < 4.0:
            cognitive_status = "Significant Cognitive Processing Impairment / Attentional Deficit"
            neurodynamics = "Substantial slowing of stimulus categorization and cortical working memory update; seen in dementia, severe depression, or traumatic encephalopathy."
        elif p300_latency_ms > upper_limit_normal_ms or p300_amplitude_uv < 7.0:
            cognitive_status = "Subclinical Cognitive Slowing / Attenuated Attentional Allocation"
            neurodynamics = "Mild delay in cortical information processing speed relative to age-matched norms; seen in mental fatigue, sleep deprivation, or early neurodegeneration."
        else:
            cognitive_status = "Optimal Cognitive Processing Speed & Robust Attentional Focus"
            neurodynamics = "Rapid stimulus evaluation and intact fronto-parietal attentional orienting networks."

        return {
            "status": "success",
            "p300_measurements": {
                "p300_latency_ms": round(p300_latency_ms, 1),
                "p300_amplitude_uv": round(p300_amplitude_uv, 2),
                "electrode_site": electrode_site
            },
            "normative_indices": {
                "patient_age_years": age,
                "predicted_latency_ms": round(predicted_latency_ms, 1),
                "upper_limit_normal_ms": round(upper_limit_normal_ms, 1),
                "latency_deviation_ms": round(latency_deviation_ms, 1),
                "reaction_time_ms": reaction_time_ms,
                "motor_execution_slack_ms": motor_slack_ms
            },
            "cognitive_assessment": {
                "cognitive_status": cognitive_status,
                "neurodynamics": neurodynamics
            }
        }
