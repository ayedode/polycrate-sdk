from typing import Literal

ApiV1ArtifactsListContentUrlErrorComponentAttr = Literal["content_url"]

API_V1_ARTIFACTS_LIST_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsListContentUrlErrorComponentAttr] = {
    "content_url",
}


def check_api_v1_artifacts_list_content_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactsListContentUrlErrorComponentAttr:
    if value in API_V1_ARTIFACTS_LIST_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
