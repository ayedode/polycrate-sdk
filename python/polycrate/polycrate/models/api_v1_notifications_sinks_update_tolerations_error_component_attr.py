from typing import Literal

ApiV1NotificationsSinksUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_notifications_sinks_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateTolerationsErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
