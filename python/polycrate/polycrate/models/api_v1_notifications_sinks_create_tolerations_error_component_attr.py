from typing import Literal

ApiV1NotificationsSinksCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_NOTIFICATIONS_SINKS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_notifications_sinks_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksCreateTolerationsErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
