from typing import Literal

PatchedEndpointRequestCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

PATCHED_ENDPOINT_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[
    PatchedEndpointRequestCreatedByComponentType2Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_endpoint_request_created_by_component_type_2_type_1(
    value: str,
) -> PatchedEndpointRequestCreatedByComponentType2Type1:
    if value in PATCHED_ENDPOINT_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ENDPOINT_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
