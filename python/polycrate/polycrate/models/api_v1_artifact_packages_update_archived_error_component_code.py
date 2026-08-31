from typing import Literal

ApiV1ArtifactPackagesUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_PACKAGES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_packages_update_archived_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesUpdateArchivedErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
