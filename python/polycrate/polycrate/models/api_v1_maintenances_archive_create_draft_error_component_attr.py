from typing import Literal

ApiV1MaintenancesArchiveCreateDraftErrorComponentAttr = Literal["draft"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateDraftErrorComponentAttr
] = {
    "draft",
}


def check_api_v1_maintenances_archive_create_draft_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateDraftErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
