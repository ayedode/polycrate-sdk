from typing import Literal

ApiV1WorkspacesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_WORKSPACES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesCreateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1_workspaces_create_archived_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateArchivedErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
