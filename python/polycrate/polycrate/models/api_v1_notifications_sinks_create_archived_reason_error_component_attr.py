from typing import Literal

ApiV1NotificationsSinksCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_notifications_sinks_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
