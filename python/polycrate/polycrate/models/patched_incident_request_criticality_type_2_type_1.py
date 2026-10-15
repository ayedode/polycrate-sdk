from typing import Literal

PatchedIncidentRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_INCIDENT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PatchedIncidentRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_incident_request_criticality_type_2_type_1(value: str) -> PatchedIncidentRequestCriticalityType2Type1:
    if value in PATCHED_INCIDENT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_INCIDENT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
