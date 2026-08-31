from typing import Literal

ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponentAttr = Literal["owner_id"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponentAttr
] = {
    "owner_id",
}


def check_api_v1_workspaces_logs_reload_create_owner_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
