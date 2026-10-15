from typing import Literal

IncidentCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

INCIDENT_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[IncidentCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_incident_created_by_component_type_1(value: str) -> IncidentCreatedByComponentType1:
    if value in INCIDENT_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}")
