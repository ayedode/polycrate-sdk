from typing import Literal

ApiV1AlertsListUntilErrorComponentCode = Literal["invalid"]

API_V1_ALERTS_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsListUntilErrorComponentCode] = {
    "invalid",
}


def check_api_v1_alerts_list_until_error_component_code(value: str) -> ApiV1AlertsListUntilErrorComponentCode:
    if value in API_V1_ALERTS_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
