from typing import Literal

ApiV1ArtifactsCreateMirroredErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACTS_CREATE_MIRRORED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsCreateMirroredErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_artifacts_create_mirrored_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreateMirroredErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_MIRRORED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_MIRRORED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
