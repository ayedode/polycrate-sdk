from typing import Literal

ArtifactRepositoryCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

ARTIFACT_REPOSITORY_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[ArtifactRepositoryCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_artifact_repository_created_by_component_type_1(value: str) -> ArtifactRepositoryCreatedByComponentType1:
    if value in ARTIFACT_REPOSITORY_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
