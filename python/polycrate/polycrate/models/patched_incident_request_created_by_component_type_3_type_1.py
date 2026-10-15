from typing import Literal

PatchedIncidentRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

PATCHED_INCIDENT_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[
    PatchedIncidentRequestCreatedByComponentType3Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_incident_request_created_by_component_type_3_type_1(
    value: str,
) -> PatchedIncidentRequestCreatedByComponentType3Type1:
    if value in PATCHED_INCIDENT_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_INCIDENT_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
