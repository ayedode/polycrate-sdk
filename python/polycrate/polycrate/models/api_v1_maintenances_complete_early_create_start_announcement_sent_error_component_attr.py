from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponentAttr = Literal["start_announcement_sent"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponentAttr
] = {
    "start_announcement_sent",
}


def check_api_v1_maintenances_complete_early_create_start_announcement_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
