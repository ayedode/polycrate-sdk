from typing import Literal

ArtifactPackageListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ARTIFACT_PACKAGE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    ArtifactPackageListEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_artifact_package_list_effective_criticality_type_2_type_1(
    value: str,
) -> ArtifactPackageListEffectiveCriticalityType2Type1:
    if value in ARTIFACT_PACKAGE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
