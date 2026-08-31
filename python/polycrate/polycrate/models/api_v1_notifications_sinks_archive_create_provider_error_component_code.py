from typing import Literal

ApiV1NotificationsSinksArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_notifications_sinks_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateProviderErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
