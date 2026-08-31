from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_maintenances_complete_early_create_workspace_id_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
