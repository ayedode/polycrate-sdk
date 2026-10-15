from typing import Literal

PatchedArtifactRepositoryRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedArtifactRepositoryRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_artifact_repository_request_criticality_type_1(
    value: str,
) -> PatchedArtifactRepositoryRequestCriticalityType1:
    if value in PATCHED_ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ARTIFACT_REPOSITORY_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
