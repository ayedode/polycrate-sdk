from typing import Literal

ApiV1NotificationsSinksCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_notifications_sinks_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksCreateArchivedAtErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
