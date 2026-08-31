from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_complete_early_create_announcement_results_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
