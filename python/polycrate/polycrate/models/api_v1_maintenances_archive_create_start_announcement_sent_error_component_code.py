from typing import Literal

ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_archive_create_start_announcement_sent_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
