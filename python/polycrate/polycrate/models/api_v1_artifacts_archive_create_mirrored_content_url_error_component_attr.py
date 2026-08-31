from typing import Literal

ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponentAttr = Literal["mirrored_content_url"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponentAttr
] = {
    "mirrored_content_url",
}


def check_api_v1_artifacts_archive_create_mirrored_content_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
