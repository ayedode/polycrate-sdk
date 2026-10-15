from typing import Literal

ArtifactCriticalityType3Type1 = Literal["", "high", "low", "medium"]

ARTIFACT_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ArtifactCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_artifact_criticality_type_3_type_1(value: str) -> ArtifactCriticalityType3Type1:
    if value in ARTIFACT_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
