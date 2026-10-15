from typing import Literal

ArtifactRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

ARTIFACT_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[ArtifactRequestCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_artifact_request_created_by_component_type_3_type_1(
    value: str,
) -> ArtifactRequestCreatedByComponentType3Type1:
    if value in ARTIFACT_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
