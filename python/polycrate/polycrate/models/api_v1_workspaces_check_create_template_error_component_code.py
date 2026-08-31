from typing import Literal

ApiV1WorkspacesCheckCreateTemplateErrorComponentCode = Literal["does_not_exist", "invalid"]

API_V1_WORKSPACES_CHECK_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateTemplateErrorComponentCode
] = {
    "does_not_exist",
    "invalid",
}


def check_api_v1_workspaces_check_create_template_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateTemplateErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
