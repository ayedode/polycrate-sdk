from typing import Literal

ApiV1ArtifactsUpdateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_ARTIFACTS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_artifacts_update_kind_error_component_code(value: str) -> ApiV1ArtifactsUpdateKindErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
