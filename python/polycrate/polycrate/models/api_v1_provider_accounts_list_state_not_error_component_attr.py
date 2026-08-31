from typing import Literal

ApiV1ProviderAccountsListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_PROVIDER_ACCOUNTS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_provider_accounts_list_state_not_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListStateNotErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
