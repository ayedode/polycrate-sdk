from typing import Literal

ArtifactRegistryListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ARTIFACT_REGISTRY_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    ArtifactRegistryListEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_artifact_registry_list_effective_criticality_type_2_type_1(
    value: str,
) -> ArtifactRegistryListEffectiveCriticalityType2Type1:
    if value in ARTIFACT_REGISTRY_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
