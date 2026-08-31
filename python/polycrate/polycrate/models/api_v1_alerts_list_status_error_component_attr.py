from typing import Literal

ApiV1AlertsListStatusErrorComponentAttr = Literal["status"]

API_V1_ALERTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsListStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_alerts_list_status_error_component_attr(value: str) -> ApiV1AlertsListStatusErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
