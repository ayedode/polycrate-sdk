from typing import Literal

ApiV1WorkspacesReloadCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_WORKSPACES_RELOAD_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_workspaces_reload_create_archived_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateArchivedErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
