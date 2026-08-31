from typing import Literal

ApiV1AlertsArchiveCreateMessageErrorComponentAttr = Literal["message"]

API_V1_ALERTS_ARCHIVE_CREATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsArchiveCreateMessageErrorComponentAttr
] = {
    "message",
}


def check_api_v1_alerts_archive_create_message_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreateMessageErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_MESSAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
