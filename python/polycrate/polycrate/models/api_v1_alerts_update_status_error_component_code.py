from typing import Literal

ApiV1AlertsUpdateStatusErrorComponentCode = Literal["invalid_choice"]

API_V1_ALERTS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateStatusErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_alerts_update_status_error_component_code(value: str) -> ApiV1AlertsUpdateStatusErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
