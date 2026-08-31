from typing import Literal

ApiV1MaintenancesCreateStartAnnouncementSentErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCreateStartAnnouncementSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_create_start_announcement_sent_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreateStartAnnouncementSentErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
