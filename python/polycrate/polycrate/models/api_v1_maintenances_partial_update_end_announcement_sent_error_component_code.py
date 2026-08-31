from typing import Literal

ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_partial_update_end_announcement_sent_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
