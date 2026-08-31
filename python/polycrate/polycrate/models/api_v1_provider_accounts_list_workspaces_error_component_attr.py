from typing import Literal

ApiV1ProviderAccountsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_PROVIDER_ACCOUNTS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_provider_accounts_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListWorkspacesErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
