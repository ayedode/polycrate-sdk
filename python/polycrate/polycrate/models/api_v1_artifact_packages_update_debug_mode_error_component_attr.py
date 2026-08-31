from typing import Literal

ApiV1ArtifactPackagesUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_ARTIFACT_PACKAGES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_artifact_packages_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateDebugModeErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
