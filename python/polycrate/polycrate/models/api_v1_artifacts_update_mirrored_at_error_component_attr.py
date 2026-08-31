from typing import Literal

ApiV1ArtifactsUpdateMirroredAtErrorComponentAttr = Literal["mirrored_at"]

API_V1_ARTIFACTS_UPDATE_MIRRORED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateMirroredAtErrorComponentAttr
] = {
    "mirrored_at",
}


def check_api_v1_artifacts_update_mirrored_at_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateMirroredAtErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_MIRRORED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_MIRRORED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
