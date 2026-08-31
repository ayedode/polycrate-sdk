from typing import Literal

ApiV1ArtifactsPartialUpdateMirroredAtErrorComponentAttr = Literal["mirrored_at"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateMirroredAtErrorComponentAttr
] = {
    "mirrored_at",
}


def check_api_v1_artifacts_partial_update_mirrored_at_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateMirroredAtErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
