from typing import Literal

ApiV1WorkspacesDiscoverCreateTemplateErrorComponentCode = Literal["does_not_exist", "invalid"]

API_V1_WORKSPACES_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesDiscoverCreateTemplateErrorComponentCode
] = {
    "does_not_exist",
    "invalid",
}


def check_api_v1_workspaces_discover_create_template_error_component_code(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateTemplateErrorComponentCode:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
