from typing import Literal

ApiV1AlertsPartialUpdateMessageErrorComponentAttr = Literal["message"]

API_V1_ALERTS_PARTIAL_UPDATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateMessageErrorComponentAttr
] = {
    "message",
}


def check_api_v1_alerts_partial_update_message_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateMessageErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
