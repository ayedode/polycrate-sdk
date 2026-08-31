from typing import Literal

ApiV1HostsUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1HostsUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
