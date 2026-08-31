from typing import Literal

ApiV1ArtifactPackagesCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_PACKAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_packages_create_platform_service_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesCreatePlatformServiceErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
