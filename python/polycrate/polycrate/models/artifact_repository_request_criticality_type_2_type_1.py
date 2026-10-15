from typing import Literal

ArtifactRepositoryRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ArtifactRepositoryRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_artifact_repository_request_criticality_type_2_type_1(
    value: str,
) -> ArtifactRepositoryRequestCriticalityType2Type1:
    if value in ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
