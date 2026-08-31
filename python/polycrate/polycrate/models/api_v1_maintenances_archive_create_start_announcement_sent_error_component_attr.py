from typing import Literal

ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponentAttr = Literal["start_announcement_sent"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponentAttr
] = {
    "start_announcement_sent",
}


def check_api_v1_maintenances_archive_create_start_announcement_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
