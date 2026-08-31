from typing import Literal

ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_notifications_sinks_archive_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateSloTargetErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
