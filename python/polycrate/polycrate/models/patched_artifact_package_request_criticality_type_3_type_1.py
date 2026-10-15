from typing import Literal

PatchedArtifactPackageRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_ARTIFACT_PACKAGE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedArtifactPackageRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_artifact_package_request_criticality_type_3_type_1(
    value: str,
) -> PatchedArtifactPackageRequestCriticalityType3Type1:
    if value in PATCHED_ARTIFACT_PACKAGE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ARTIFACT_PACKAGE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
