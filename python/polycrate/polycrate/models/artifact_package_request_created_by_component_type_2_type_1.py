from typing import Literal

ArtifactPackageRequestCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

ARTIFACT_PACKAGE_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[
    ArtifactPackageRequestCreatedByComponentType2Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_artifact_package_request_created_by_component_type_2_type_1(
    value: str,
) -> ArtifactPackageRequestCreatedByComponentType2Type1:
    if value in ARTIFACT_PACKAGE_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
