from typing import Literal

ApiV1WorkspacesReloadCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACES_RELOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspaces_reload_create_description_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
