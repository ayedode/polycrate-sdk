from typing import Literal

ApiV1ArtifactsUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ARTIFACTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_artifacts_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
