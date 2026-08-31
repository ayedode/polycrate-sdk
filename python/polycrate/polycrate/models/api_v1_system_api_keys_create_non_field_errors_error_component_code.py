from typing import Literal

ApiV1SystemApiKeysCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_SYSTEM_API_KEYS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SystemApiKeysCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_system_api_keys_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1SystemApiKeysCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_SYSTEM_API_KEYS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SYSTEM_API_KEYS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
