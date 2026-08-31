from typing import Literal

ApiV1MaintenancesArchiveCreateEndErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow", "required"
]

API_V1_MAINTENANCES_ARCHIVE_CREATE_END_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateEndErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
    "required",
}


def check_api_v1_maintenances_archive_create_end_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateEndErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_END_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_END_ERROR_COMPONENT_CODE_VALUES!r}"
    )
