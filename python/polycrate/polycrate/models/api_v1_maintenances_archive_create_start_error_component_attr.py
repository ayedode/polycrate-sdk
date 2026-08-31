from typing import Literal

ApiV1MaintenancesArchiveCreateStartErrorComponentAttr = Literal["start"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateStartErrorComponentAttr
] = {
    "start",
}


def check_api_v1_maintenances_archive_create_start_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateStartErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
