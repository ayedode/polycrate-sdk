from typing import Literal

ArtifactRegistryListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

ARTIFACT_REGISTRY_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    ArtifactRegistryListEffectiveCriticalityType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_artifact_registry_list_effective_criticality_type_3_type_1(
    value: str,
) -> ArtifactRegistryListEffectiveCriticalityType3Type1:
    if value in ARTIFACT_REGISTRY_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
