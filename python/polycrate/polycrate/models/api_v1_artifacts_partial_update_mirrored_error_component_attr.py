from typing import Literal

ApiV1ArtifactsPartialUpdateMirroredErrorComponentAttr = Literal["mirrored"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateMirroredErrorComponentAttr
] = {
    "mirrored",
}


def check_api_v1_artifacts_partial_update_mirrored_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateMirroredErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
