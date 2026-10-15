from typing import Literal

PatchedIncidentRequestKind = Literal[
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

PATCHED_INCIDENT_REQUEST_KIND_VALUES: set[PatchedIncidentRequestKind] = {
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


def check_patched_incident_request_kind(value: str) -> PatchedIncidentRequestKind:
    if value in PATCHED_INCIDENT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_INCIDENT_REQUEST_KIND_VALUES!r}")
