from typing import Literal

ApiV1AlertsDiscoverCreateMessageErrorComponentAttr = Literal["message"]

API_V1_ALERTS_DISCOVER_CREATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateMessageErrorComponentAttr
] = {
    "message",
}


def check_api_v1_alerts_discover_create_message_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateMessageErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
