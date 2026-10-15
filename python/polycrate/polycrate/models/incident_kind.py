from typing import Literal

IncidentKind = Literal[
    "account-compromise",
    "availability",
    "data-breach",
    "data-leak",
    "integrity",
    "malware",
    "network-attack",
    "other",
    "phishing",
    "physical",
    "policy-violation",
    "security-control",
    "supply-chain",
    "unauthorized-access",
    "upstream-provider",
]

INCIDENT_KIND_VALUES: set[IncidentKind] = {
    "account-compromise",
    "availability",
    "data-breach",
    "data-leak",
    "integrity",
    "malware",
    "network-attack",
    "other",
    "phishing",
    "physical",
    "policy-violation",
    "security-control",
    "supply-chain",
    "unauthorized-access",
    "upstream-provider",
}


def check_incident_kind(value: str) -> IncidentKind:
    if value in INCIDENT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_KIND_VALUES!r}")
