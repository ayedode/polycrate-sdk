from typing import Literal

ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_PREFIXES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_prefixes_partial_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1PrefixesPartialUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
