from typing import Literal

ApiV1ArtifactsCreateContentUrlErrorComponentAttr = Literal["content_url"]

API_V1_ARTIFACTS_CREATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsCreateContentUrlErrorComponentAttr
] = {
    "content_url",
}


def check_api_v1_artifacts_create_content_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateContentUrlErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
