from typing import Literal

ApiV1ArtifactsPartialUpdateMirroredErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsPartialUpdateMirroredErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifacts_partial_update_mirrored_error_component_code(
    value: str,
) -> ApiV1ArtifactsPartialUpdateMirroredErrorComponentCode:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_MIRRORED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
