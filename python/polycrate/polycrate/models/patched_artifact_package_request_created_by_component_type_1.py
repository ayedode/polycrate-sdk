from typing import Literal

PatchedArtifactPackageRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

PATCHED_ARTIFACT_PACKAGE_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[
    PatchedArtifactPackageRequestCreatedByComponentType1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_artifact_package_request_created_by_component_type_1(
    value: str,
) -> PatchedArtifactPackageRequestCreatedByComponentType1:
    if value in PATCHED_ARTIFACT_PACKAGE_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ARTIFACT_PACKAGE_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
