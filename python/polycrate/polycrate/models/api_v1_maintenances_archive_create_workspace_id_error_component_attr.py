from typing import Literal

ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_maintenances_archive_create_workspace_id_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
