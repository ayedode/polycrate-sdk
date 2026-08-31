from typing import Literal

ApiV1ProviderAccountsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_provider_accounts_update_archived_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateArchivedErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
