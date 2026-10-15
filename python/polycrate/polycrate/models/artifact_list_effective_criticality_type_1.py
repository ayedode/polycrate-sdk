from typing import Literal

ArtifactListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ARTIFACT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ArtifactListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_artifact_list_effective_criticality_type_1(value: str) -> ArtifactListEffectiveCriticalityType1:
    if value in ARTIFACT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
