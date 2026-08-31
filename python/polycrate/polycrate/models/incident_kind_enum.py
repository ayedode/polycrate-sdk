from typing import Literal

IncidentKindEnum = Literal[
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

INCIDENT_KIND_ENUM_VALUES: set[IncidentKindEnum] = {
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


def check_incident_kind_enum(value: str) -> IncidentKindEnum:
    if value in INCIDENT_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_KIND_ENUM_VALUES!r}")
