from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_complete_early_create_end_announcement_sent_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
