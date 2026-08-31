from typing import Literal

ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponentAttr = Literal["announcement_sent"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponentAttr
] = {
    "announcement_sent",
}


def check_api_v1_maintenances_partial_update_announcement_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_ANNOUNCEMENT_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
