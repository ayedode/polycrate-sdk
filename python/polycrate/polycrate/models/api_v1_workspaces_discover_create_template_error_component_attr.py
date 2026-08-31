from typing import Literal

ApiV1WorkspacesDiscoverCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_WORKSPACES_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_workspaces_discover_create_template_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateTemplateErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
