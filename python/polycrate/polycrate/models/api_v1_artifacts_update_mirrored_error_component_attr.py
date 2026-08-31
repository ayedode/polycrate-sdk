from typing import Literal

ApiV1ArtifactsUpdateMirroredErrorComponentAttr = Literal["mirrored"]

API_V1_ARTIFACTS_UPDATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsUpdateMirroredErrorComponentAttr] = {
    "mirrored",
}


def check_api_v1_artifacts_update_mirrored_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateMirroredErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
