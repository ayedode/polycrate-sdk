from typing import Literal

ArtifactRepositoryRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

ARTIFACT_REPOSITORY_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[
    ArtifactRepositoryRequestCreatedByComponentType1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_artifact_repository_request_created_by_component_type_1(
    value: str,
) -> ArtifactRepositoryRequestCreatedByComponentType1:
    if value in ARTIFACT_REPOSITORY_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
