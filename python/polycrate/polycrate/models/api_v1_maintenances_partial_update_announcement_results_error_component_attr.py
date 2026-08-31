from typing import Literal

ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponentAttr = Literal["announcement_results"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponentAttr
] = {
    "announcement_results",
}


def check_api_v1_maintenances_partial_update_announcement_results_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
