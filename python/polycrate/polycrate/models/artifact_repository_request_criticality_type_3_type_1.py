from typing import Literal

ArtifactRepositoryRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ArtifactRepositoryRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_artifact_repository_request_criticality_type_3_type_1(
    value: str,
) -> ArtifactRepositoryRequestCriticalityType3Type1:
    if value in ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
