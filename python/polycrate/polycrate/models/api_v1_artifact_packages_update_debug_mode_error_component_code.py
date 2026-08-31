from typing import Literal

ApiV1ArtifactPackagesUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_PACKAGES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_packages_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesUpdateDebugModeErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
