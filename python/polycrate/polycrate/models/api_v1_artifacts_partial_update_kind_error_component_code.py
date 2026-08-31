from typing import Literal

ApiV1ArtifactsPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_artifacts_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1ArtifactsPartialUpdateKindErrorComponentCode:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
