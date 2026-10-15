from typing import Literal

IncidentRequestKind = Literal[
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

INCIDENT_REQUEST_KIND_VALUES: set[IncidentRequestKind] = {
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


def check_incident_request_kind(value: str) -> IncidentRequestKind:
    if value in INCIDENT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_REQUEST_KIND_VALUES!r}")
