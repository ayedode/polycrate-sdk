from typing import Literal

ApiV1AlertsCreateStatusErrorComponentCode = Literal["invalid_choice"]

API_V1_ALERTS_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsCreateStatusErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_alerts_create_status_error_component_code(value: str) -> ApiV1AlertsCreateStatusErrorComponentCode:
    if value in API_V1_ALERTS_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
