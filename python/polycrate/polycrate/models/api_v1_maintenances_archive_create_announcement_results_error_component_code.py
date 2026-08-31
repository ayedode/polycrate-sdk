from typing import Literal

ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_archive_create_announcement_results_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_ANNOUNCEMENT_RESULTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
