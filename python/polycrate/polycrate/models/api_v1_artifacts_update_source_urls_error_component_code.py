from typing import Literal

ApiV1ArtifactsUpdateSourceUrlsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACTS_UPDATE_SOURCE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsUpdateSourceUrlsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifacts_update_source_urls_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateSourceUrlsErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_SOURCE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_SOURCE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
