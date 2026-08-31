from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_repositories_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
