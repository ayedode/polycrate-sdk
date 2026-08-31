from typing import Literal

ApiV1PoliciesUpdateWorkspacesSelectorErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_UPDATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesUpdateWorkspacesSelectorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_update_workspaces_selector_error_component_code(
    value: str,
) -> ApiV1PoliciesUpdateWorkspacesSelectorErrorComponentCode:
    if value in API_V1_POLICIES_UPDATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
