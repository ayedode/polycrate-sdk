from typing import Literal

ApiV1ArtifactsUpdateSourceUrlsErrorComponentAttr = Literal["source_urls"]

API_V1_ARTIFACTS_UPDATE_SOURCE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateSourceUrlsErrorComponentAttr
] = {
    "source_urls",
}


def check_api_v1_artifacts_update_source_urls_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateSourceUrlsErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_SOURCE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_SOURCE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
