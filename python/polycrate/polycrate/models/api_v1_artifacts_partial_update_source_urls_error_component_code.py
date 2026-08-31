from typing import Literal

ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_SOURCE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifacts_partial_update_source_urls_error_component_code(
    value: str,
) -> ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponentCode:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_SOURCE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_SOURCE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
