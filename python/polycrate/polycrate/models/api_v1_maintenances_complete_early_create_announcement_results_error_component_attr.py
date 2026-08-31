from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponentAttr = Literal["announcement_results"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponentAttr
] = {
    "announcement_results",
}


def check_api_v1_maintenances_complete_early_create_announcement_results_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
