from typing import Literal

ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_artifact_repositories_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
