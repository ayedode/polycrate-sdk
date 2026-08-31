from typing import Literal

ApiV1WorkspacesCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_WORKSPACES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_workspaces_create_display_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateDisplayNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
