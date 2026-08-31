from typing import Literal

ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ARTIFACT_PACKAGES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_artifact_packages_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
