from typing import Literal

ApiV1WorkspacesReloadCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_WORKSPACES_RELOAD_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_workspaces_reload_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateArchivedAtErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
