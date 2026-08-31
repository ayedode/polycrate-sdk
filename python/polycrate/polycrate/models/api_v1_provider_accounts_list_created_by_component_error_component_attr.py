from typing import Literal

ApiV1ProviderAccountsListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_PROVIDER_ACCOUNTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_provider_accounts_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListCreatedByComponentErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
