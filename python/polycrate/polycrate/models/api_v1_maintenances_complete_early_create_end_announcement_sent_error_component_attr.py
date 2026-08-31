from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponentAttr = Literal["end_announcement_sent"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponentAttr
] = {
    "end_announcement_sent",
}


def check_api_v1_maintenances_complete_early_create_end_announcement_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_END_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
