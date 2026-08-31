from typing import Literal

ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponentAttr = Literal["announcement_results"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponentAttr
] = {
    "announcement_results",
}


def check_api_v1_maintenances_archive_create_announcement_results_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
