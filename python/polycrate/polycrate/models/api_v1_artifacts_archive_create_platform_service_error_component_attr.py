from typing import Literal

ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_artifacts_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
