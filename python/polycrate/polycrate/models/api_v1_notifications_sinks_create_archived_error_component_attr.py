from typing import Literal

ApiV1NotificationsSinksCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_notifications_sinks_create_archived_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksCreateArchivedErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
