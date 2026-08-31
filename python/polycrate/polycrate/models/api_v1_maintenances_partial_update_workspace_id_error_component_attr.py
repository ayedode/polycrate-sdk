from typing import Literal

ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_maintenances_partial_update_workspace_id_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
