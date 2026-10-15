from typing import Literal

ArtifactRepositoryRequestCriticalityType1 = Literal["", "high", "low", "medium"]

ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_1_VALUES: set[ArtifactRepositoryRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_artifact_repository_request_criticality_type_1(value: str) -> ArtifactRepositoryRequestCriticalityType1:
    if value in ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
