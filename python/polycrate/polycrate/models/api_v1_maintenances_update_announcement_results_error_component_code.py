from typing import Literal

ApiV1MaintenancesUpdateAnnouncementResultsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_UPDATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesUpdateAnnouncementResultsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_update_announcement_results_error_component_code(
    value: str,
) -> ApiV1MaintenancesUpdateAnnouncementResultsErrorComponentCode:
    if value in API_V1_MAINTENANCES_UPDATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
