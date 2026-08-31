from typing import Literal

ApiV1WorkspacesCreateNameErrorComponentAttr = Literal["name"]

API_V1_WORKSPACES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_workspaces_create_name_error_component_attr(value: str) -> ApiV1WorkspacesCreateNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
