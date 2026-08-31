from typing import Literal

ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponentAttr = Literal[
    "monitoring_workspace_allowlist_ids"
]

API_V1_WORKSPACES_ARCHIVE_CREATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponentAttr
] = {
    "monitoring_workspace_allowlist_ids",
}


def check_api_v1_workspaces_archive_create_monitoring_workspace_allowlist_ids_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
