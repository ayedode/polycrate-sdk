from typing import Literal

ApiV1AlertsListUntilErrorComponentAttr = Literal["until"]

API_V1_ALERTS_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsListUntilErrorComponentAttr] = {
    "until",
}


def check_api_v1_alerts_list_until_error_component_attr(value: str) -> ApiV1AlertsListUntilErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
