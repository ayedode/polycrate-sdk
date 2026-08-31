from typing import Literal

ApiV1WorkspacesUpdateTemplateErrorComponentAttr = Literal["template"]

API_V1_WORKSPACES_UPDATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesUpdateTemplateErrorComponentAttr] = {
    "template",
}


def check_api_v1_workspaces_update_template_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateTemplateErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
