from typing import Literal

ArtifactCriticalityType2Type1 = Literal["", "high", "low", "medium"]

ARTIFACT_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ArtifactCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_artifact_criticality_type_2_type_1(value: str) -> ArtifactCriticalityType2Type1:
    if value in ARTIFACT_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
