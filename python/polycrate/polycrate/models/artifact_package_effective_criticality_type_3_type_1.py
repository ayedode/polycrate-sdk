from typing import Literal

ArtifactPackageEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

ARTIFACT_PACKAGE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ArtifactPackageEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_artifact_package_effective_criticality_type_3_type_1(
    value: str,
) -> ArtifactPackageEffectiveCriticalityType3Type1:
    if value in ARTIFACT_PACKAGE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
