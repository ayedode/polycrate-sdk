from typing import Literal

ArtifactPackageCriticalityType1 = Literal["", "high", "low", "medium"]

ARTIFACT_PACKAGE_CRITICALITY_TYPE_1_VALUES: set[ArtifactPackageCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_artifact_package_criticality_type_1(value: str) -> ArtifactPackageCriticalityType1:
    if value in ARTIFACT_PACKAGE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_CRITICALITY_TYPE_1_VALUES!r}")
