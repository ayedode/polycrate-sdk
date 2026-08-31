from typing import Literal

ApiV1WorkspacesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_WORKSPACES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_workspaces_update_name_error_component_attr(value: str) -> ApiV1WorkspacesUpdateNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
