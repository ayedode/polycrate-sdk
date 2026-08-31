from typing import Literal

ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_UPDATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_update_start_announcement_sent_error_component_code(
    value: str,
) -> ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponentCode:
    if value in API_V1_MAINTENANCES_UPDATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
