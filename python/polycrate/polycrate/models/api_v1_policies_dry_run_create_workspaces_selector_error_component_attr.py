from typing import Literal

ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponentAttr = Literal["workspaces_selector"]

API_V1_POLICIES_DRY_RUN_CREATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponentAttr
] = {
    "workspaces_selector",
}


def check_api_v1_policies_dry_run_create_workspaces_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateWorkspacesSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_WORKSPACES_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
