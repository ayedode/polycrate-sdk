from typing import Literal

ApiV1ArtifactsCreateMirroredErrorComponentAttr = Literal["mirrored"]

API_V1_ARTIFACTS_CREATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsCreateMirroredErrorComponentAttr] = {
    "mirrored",
}


def check_api_v1_artifacts_create_mirrored_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateMirroredErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
