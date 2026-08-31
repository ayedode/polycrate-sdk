from typing import Literal

ApiV1WorkspacesReloadCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_WORKSPACES_RELOAD_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_workspaces_reload_create_display_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateDisplayNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
