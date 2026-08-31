from typing import Literal

ApiV1WorkspacesReloadCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_WORKSPACES_RELOAD_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_workspaces_reload_create_template_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateTemplateErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
