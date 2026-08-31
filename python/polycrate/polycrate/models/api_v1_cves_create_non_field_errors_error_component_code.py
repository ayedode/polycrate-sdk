from typing import Literal

ApiV1CvesCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_CVES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CvesCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_cves_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1CvesCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_CVES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
