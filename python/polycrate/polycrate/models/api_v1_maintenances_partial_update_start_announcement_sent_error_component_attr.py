from typing import Literal

ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponentAttr = Literal["start_announcement_sent"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponentAttr
] = {
    "start_announcement_sent",
}


def check_api_v1_maintenances_partial_update_start_announcement_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_START_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
