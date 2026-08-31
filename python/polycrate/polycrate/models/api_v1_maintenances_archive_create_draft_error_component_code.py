from typing import Literal

ApiV1MaintenancesArchiveCreateDraftErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_DRAFT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateDraftErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_archive_create_draft_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateDraftErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_DRAFT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_DRAFT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
