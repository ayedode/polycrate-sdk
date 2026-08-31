from typing import Literal

ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_notifications_sinks_archive_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
