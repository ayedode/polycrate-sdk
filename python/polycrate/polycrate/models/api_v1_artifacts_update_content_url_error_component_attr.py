from typing import Literal

ApiV1ArtifactsUpdateContentUrlErrorComponentAttr = Literal["content_url"]

API_V1_ARTIFACTS_UPDATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateContentUrlErrorComponentAttr
] = {
    "content_url",
}


def check_api_v1_artifacts_update_content_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateContentUrlErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
