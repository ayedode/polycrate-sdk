from typing import Literal

ArtifactRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

ARTIFACT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ArtifactRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_artifact_request_criticality_type_2_type_1(value: str) -> ArtifactRequestCriticalityType2Type1:
    if value in ARTIFACT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
