from typing import Literal

ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_provider_accounts_archive_create_workspace_id_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
