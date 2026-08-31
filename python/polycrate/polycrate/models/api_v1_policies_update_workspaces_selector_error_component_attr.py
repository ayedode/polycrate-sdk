from typing import Literal

ApiV1PoliciesUpdateWorkspacesSelectorErrorComponentAttr = Literal["workspaces_selector"]

API_V1_POLICIES_UPDATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesUpdateWorkspacesSelectorErrorComponentAttr
] = {
    "workspaces_selector",
}


def check_api_v1_policies_update_workspaces_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesUpdateWorkspacesSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
