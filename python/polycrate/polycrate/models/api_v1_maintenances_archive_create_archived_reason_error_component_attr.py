from typing import Literal

ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_maintenances_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
