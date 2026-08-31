from typing import Literal

ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_artifact_packages_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
