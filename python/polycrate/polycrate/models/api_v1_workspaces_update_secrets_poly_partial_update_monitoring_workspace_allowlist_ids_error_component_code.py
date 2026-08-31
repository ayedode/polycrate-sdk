from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_monitoring_workspace_allowlist_ids_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponentCode:
    if (
        value
        in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
