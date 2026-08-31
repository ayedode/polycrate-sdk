from typing import Literal

ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_SOURCE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifacts_archive_create_source_urls_error_component_code(
    value: str,
) -> ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponentCode:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_SOURCE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_SOURCE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
