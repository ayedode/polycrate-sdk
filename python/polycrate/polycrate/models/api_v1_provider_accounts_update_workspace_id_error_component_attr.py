from typing import Literal

ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_provider_accounts_update_workspace_id_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
