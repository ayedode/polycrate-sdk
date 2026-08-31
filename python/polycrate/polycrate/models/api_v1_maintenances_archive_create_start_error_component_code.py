from typing import Literal

ApiV1MaintenancesArchiveCreateStartErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow", "required"
]

API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateStartErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
    "required",
}


def check_api_v1_maintenances_archive_create_start_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateStartErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_START_ERROR_COMPONENT_CODE_VALUES!r}"
    )
