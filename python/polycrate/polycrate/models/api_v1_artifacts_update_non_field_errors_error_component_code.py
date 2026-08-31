from typing import Literal

ApiV1ArtifactsUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifacts_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
