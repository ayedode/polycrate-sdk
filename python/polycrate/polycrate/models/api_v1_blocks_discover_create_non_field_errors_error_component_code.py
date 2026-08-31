from typing import Literal

ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_BLOCKS_DISCOVER_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_blocks_discover_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
