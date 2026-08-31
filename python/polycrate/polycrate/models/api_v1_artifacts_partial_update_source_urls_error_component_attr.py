from typing import Literal

ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponentAttr = Literal["source_urls"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_SOURCE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponentAttr
] = {
    "source_urls",
}


def check_api_v1_artifacts_partial_update_source_urls_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_SOURCE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_SOURCE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
