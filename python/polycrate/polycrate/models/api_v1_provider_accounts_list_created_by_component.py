from typing import Literal

ApiV1ProviderAccountsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_PROVIDER_ACCOUNTS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1ProviderAccountsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_provider_accounts_list_created_by_component(value: str) -> ApiV1ProviderAccountsListCreatedByComponent:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
