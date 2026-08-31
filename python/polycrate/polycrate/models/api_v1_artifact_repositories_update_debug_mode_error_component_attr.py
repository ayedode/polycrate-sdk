from typing import Literal

ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_artifact_repositories_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
