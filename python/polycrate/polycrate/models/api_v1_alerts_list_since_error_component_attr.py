from typing import Literal

ApiV1AlertsListSinceErrorComponentAttr = Literal["since"]

API_V1_ALERTS_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsListSinceErrorComponentAttr] = {
    "since",
}


def check_api_v1_alerts_list_since_error_component_attr(value: str) -> ApiV1AlertsListSinceErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
