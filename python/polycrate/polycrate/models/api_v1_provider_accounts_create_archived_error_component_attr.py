from typing import Literal

ApiV1ProviderAccountsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_provider_accounts_create_archived_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateArchivedErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
