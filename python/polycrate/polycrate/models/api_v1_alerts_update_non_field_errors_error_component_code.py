from typing import Literal

ApiV1AlertsUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alerts_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1AlertsUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
