from typing import Literal

ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_notifications_sinks_partial_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
