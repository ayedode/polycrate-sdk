from typing import Literal

ApiV1AlertsListSinceErrorComponentCode = Literal["invalid"]

API_V1_ALERTS_LIST_SINCE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsListSinceErrorComponentCode] = {
    "invalid",
}


def check_api_v1_alerts_list_since_error_component_code(value: str) -> ApiV1AlertsListSinceErrorComponentCode:
    if value in API_V1_ALERTS_LIST_SINCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_SINCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
