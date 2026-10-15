from typing import Literal

ArtifactEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ARTIFACT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ArtifactEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_artifact_effective_criticality_type_2_type_1(value: str) -> ArtifactEffectiveCriticalityType2Type1:
    if value in ARTIFACT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
