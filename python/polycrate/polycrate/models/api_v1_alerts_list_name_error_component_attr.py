from typing import Literal

ApiV1AlertsListNameErrorComponentAttr = Literal["name"]

API_V1_ALERTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_alerts_list_name_error_component_attr(value: str) -> ApiV1AlertsListNameErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
