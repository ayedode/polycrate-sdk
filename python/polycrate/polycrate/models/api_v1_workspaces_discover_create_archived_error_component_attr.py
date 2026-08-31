from typing import Literal

ApiV1WorkspacesDiscoverCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_WORKSPACES_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_workspaces_discover_create_archived_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateArchivedErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
