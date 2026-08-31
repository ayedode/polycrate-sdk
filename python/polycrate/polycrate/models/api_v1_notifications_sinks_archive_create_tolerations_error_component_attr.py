from typing import Literal

ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_notifications_sinks_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
