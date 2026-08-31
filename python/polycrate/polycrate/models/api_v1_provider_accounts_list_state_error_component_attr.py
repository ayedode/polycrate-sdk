from typing import Literal

ApiV1ProviderAccountsListStateErrorComponentAttr = Literal["state"]

API_V1_PROVIDER_ACCOUNTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_provider_accounts_list_state_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListStateErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
