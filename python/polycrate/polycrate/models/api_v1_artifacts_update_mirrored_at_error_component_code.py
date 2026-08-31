from typing import Literal

ApiV1ArtifactsUpdateMirroredAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ARTIFACTS_UPDATE_MIRRORED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsUpdateMirroredAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_artifacts_update_mirrored_at_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateMirroredAtErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_MIRRORED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_MIRRORED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
