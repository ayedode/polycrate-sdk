from typing import Literal

ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_artifact_packages_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
