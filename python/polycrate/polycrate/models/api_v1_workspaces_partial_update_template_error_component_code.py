from typing import Literal

ApiV1WorkspacesPartialUpdateTemplateErrorComponentCode = Literal["does_not_exist", "invalid"]

API_V1_WORKSPACES_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesPartialUpdateTemplateErrorComponentCode
] = {
    "does_not_exist",
    "invalid",
}


def check_api_v1_workspaces_partial_update_template_error_component_code(
    value: str,
) -> ApiV1WorkspacesPartialUpdateTemplateErrorComponentCode:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
