from typing import Literal

ApiV1MaintenancesArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_maintenances_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateKindErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
