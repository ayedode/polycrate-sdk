from typing import Literal

ApiV1WorkspacesRepairCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_WORKSPACES_REPAIR_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_workspaces_repair_create_template_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateTemplateErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
