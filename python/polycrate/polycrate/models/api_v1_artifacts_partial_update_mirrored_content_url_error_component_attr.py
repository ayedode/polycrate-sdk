from typing import Literal

ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponentAttr = Literal["mirrored_content_url"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponentAttr
] = {
    "mirrored_content_url",
}


def check_api_v1_artifacts_partial_update_mirrored_content_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
