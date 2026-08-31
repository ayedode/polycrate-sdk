from typing import Literal

ApiV1AlertsUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_ALERTS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_alerts_update_status_error_component_attr(value: str) -> ApiV1AlertsUpdateStatusErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
