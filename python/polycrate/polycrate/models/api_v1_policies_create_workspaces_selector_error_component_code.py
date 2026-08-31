from typing import Literal

ApiV1PoliciesCreateWorkspacesSelectorErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_CREATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesCreateWorkspacesSelectorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_create_workspaces_selector_error_component_code(
    value: str,
) -> ApiV1PoliciesCreateWorkspacesSelectorErrorComponentCode:
    if value in API_V1_POLICIES_CREATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
