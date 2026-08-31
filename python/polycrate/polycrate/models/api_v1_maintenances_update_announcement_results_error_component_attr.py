from typing import Literal

ApiV1MaintenancesUpdateAnnouncementResultsErrorComponentAttr = Literal["announcement_results"]

API_V1_MAINTENANCES_UPDATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateAnnouncementResultsErrorComponentAttr
] = {
    "announcement_results",
}


def check_api_v1_maintenances_update_announcement_results_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateAnnouncementResultsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
