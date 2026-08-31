from typing import Literal

ApiV1ArtifactPackagesCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ARTIFACT_PACKAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_artifact_packages_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
