from typing import Literal

ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_archive_create_end_announcement_sent_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
