from typing import Literal

IncidentRequestCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

INCIDENT_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[IncidentRequestCreatedByComponentType2Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_incident_request_created_by_component_type_2_type_1(
    value: str,
) -> IncidentRequestCreatedByComponentType2Type1:
    if value in INCIDENT_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
