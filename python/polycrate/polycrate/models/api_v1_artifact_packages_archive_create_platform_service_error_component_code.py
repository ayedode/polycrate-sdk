from typing import Literal

ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_packages_archive_create_platform_service_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
