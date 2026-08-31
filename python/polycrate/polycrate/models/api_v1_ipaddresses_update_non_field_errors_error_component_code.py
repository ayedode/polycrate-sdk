from typing import Literal

ApiV1IpaddressesUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_IPADDRESSES_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_ipaddresses_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1IpaddressesUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_IPADDRESSES_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
