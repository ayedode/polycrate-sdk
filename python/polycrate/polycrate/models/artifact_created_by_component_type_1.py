from typing import Literal

ArtifactCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

ARTIFACT_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[ArtifactCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_artifact_created_by_component_type_1(value: str) -> ArtifactCreatedByComponentType1:
    if value in ARTIFACT_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}")
