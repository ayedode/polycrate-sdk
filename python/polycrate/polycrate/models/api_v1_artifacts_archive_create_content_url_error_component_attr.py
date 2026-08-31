from typing import Literal

ApiV1ArtifactsArchiveCreateContentUrlErrorComponentAttr = Literal["content_url"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateContentUrlErrorComponentAttr
] = {
    "content_url",
}


def check_api_v1_artifacts_archive_create_content_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateContentUrlErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
