from typing import Literal

ApiV1AlertsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_ALERTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_alerts_update_name_error_component_attr(value: str) -> ApiV1AlertsUpdateNameErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
