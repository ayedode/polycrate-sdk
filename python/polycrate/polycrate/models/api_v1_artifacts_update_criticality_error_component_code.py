from typing import Literal

ApiV1ArtifactsUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACTS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_artifacts_update_criticality_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateCriticalityErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
