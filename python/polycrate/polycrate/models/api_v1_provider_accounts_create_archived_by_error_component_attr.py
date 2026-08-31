from typing import Literal

ApiV1ProviderAccountsCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_provider_accounts_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateArchivedByErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
