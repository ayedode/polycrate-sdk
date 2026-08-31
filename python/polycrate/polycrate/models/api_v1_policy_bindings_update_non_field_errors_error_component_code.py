from typing import Literal

ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICY_BINDINGS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policy_bindings_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
