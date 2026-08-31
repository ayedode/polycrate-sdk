from typing import Literal

ApiV1WorkspacesReloadCreateOwnerIdErrorComponentAttr = Literal["owner_id"]

API_V1_WORKSPACES_RELOAD_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateOwnerIdErrorComponentAttr
] = {
    "owner_id",
}


def check_api_v1_workspaces_reload_create_owner_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateOwnerIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
