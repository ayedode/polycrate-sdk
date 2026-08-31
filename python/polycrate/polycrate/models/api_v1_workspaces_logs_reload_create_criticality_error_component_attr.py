from typing import Literal

ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_workspaces_logs_reload_create_criticality_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
