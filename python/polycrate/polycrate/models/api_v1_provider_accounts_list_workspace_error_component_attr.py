from typing import Literal

ApiV1ProviderAccountsListWorkspaceErrorComponentAttr = Literal["workspace"]

API_V1_PROVIDER_ACCOUNTS_LIST_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListWorkspaceErrorComponentAttr
] = {
    "workspace",
}


def check_api_v1_provider_accounts_list_workspace_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListWorkspaceErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
