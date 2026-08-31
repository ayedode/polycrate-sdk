from typing import Literal

ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifacts_archive_create_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
