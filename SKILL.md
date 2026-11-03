---
name: genpark-personal-agent-somatosensory-cognitive-p300-erp-latency-skill
version: 1.0.0
description: Calculates Event-Related Potential P300 Peak Latency (ms), P300 Amplitude (uV), Age-Adjusted Latency Deviation, and Motor Processing Slack using oddball paradigm electrophysiology.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - neurophysiology
  - cognitive
  - p300
  - erp
  - zero-dependency
---

# Cognitive Event-Related Potential P300 Latency Skill

## Mathematical Formulation

Age-adjusted normative P300 latency regression:

$$L_{\text{pred}} = 300.0 + 1.25 \times (\text{Age} - 20) \quad (\text{ms})$$

Upper Limit of Normal (ULN, $\approx +2\sigma$):

$$\text{ULN} = L_{\text{pred}} + 35.0 \quad (\text{ms})$$

Latency deviation:

$$\Delta L = L_{\text{P300}} - L_{\text{pred}} \quad (\text{ms})$$

Motor processing slack time:

$$\text{Slack} = \text{Reaction Time} - L_{\text{P300}} \quad (\text{ms})$$

## Clinical Cognitive Classification
- **Optimal Processing Speed**: $L_{\text{P300}} \le \text{ULN}$, Amplitude $\ge 7.0 \, \mu\text{V}$
- **Subclinical Processing Delay**: $L_{\text{P300}} > \text{ULN}$ or Amplitude $\in [4.0, 7.0] \, \mu\text{V}$ (attentional exhaustion, sleep debt, early MCI)
- **Significant Cognitive Impairment**: $L_{\text{P300}} > 450\text{ ms}$ or Amplitude $< 4.0 \, \mu\text{V}$ (marked cortical neurodegeneration)
