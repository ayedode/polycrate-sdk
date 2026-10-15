from typing import Literal

IncidentRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

INCIDENT_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[IncidentRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_incident_request_criticality_type_3_type_1(value: str) -> IncidentRequestCriticalityType3Type1:
    if value in INCIDENT_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
