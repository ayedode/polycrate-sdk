from typing import Literal

ArtifactRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

ARTIFACT_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[ArtifactRequestCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_artifact_request_created_by_component_type_1(value: str) -> ArtifactRequestCreatedByComponentType1:
    if value in ARTIFACT_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
