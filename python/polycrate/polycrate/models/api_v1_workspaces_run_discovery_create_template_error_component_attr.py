from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_workspaces_run_discovery_create_template_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateTemplateErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
