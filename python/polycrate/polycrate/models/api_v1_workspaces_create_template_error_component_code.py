from typing import Literal

ApiV1WorkspacesCreateTemplateErrorComponentCode = Literal["does_not_exist", "invalid"]

API_V1_WORKSPACES_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1WorkspacesCreateTemplateErrorComponentCode] = {
    "does_not_exist",
    "invalid",
}


def check_api_v1_workspaces_create_template_error_component_code(
    value: str,
) -> ApiV1WorkspacesCreateTemplateErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
