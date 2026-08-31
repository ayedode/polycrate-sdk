from typing import Literal

ApiV1EndpointsCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_ENDPOINTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_endpoints_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1EndpointsCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
