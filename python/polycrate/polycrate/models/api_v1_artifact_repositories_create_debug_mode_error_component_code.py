from typing import Literal

ApiV1ArtifactRepositoriesCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_repositories_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateDebugModeErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
