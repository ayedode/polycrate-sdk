from typing import Literal

PatchedArtifactRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_ARTIFACT_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedArtifactRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_artifact_request_criticality_type_1(value: str) -> PatchedArtifactRequestCriticalityType1:
    if value in PATCHED_ARTIFACT_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ARTIFACT_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
