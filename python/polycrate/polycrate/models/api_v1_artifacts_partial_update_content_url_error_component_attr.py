from typing import Literal

ApiV1ArtifactsPartialUpdateContentUrlErrorComponentAttr = Literal["content_url"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateContentUrlErrorComponentAttr
] = {
    "content_url",
}


def check_api_v1_artifacts_partial_update_content_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateContentUrlErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
