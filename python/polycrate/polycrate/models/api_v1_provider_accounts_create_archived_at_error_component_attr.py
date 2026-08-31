from typing import Literal

ApiV1ProviderAccountsCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_provider_accounts_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateArchivedAtErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
