from typing import Literal

ApiV1NotificationsSinksCreateKindErrorComponentAttr = Literal["kind"]

API_V1_NOTIFICATIONS_SINKS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_notifications_sinks_create_kind_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksCreateKindErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
