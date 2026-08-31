from typing import Literal

ApiV1ProviderAccountsCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_PROVIDER_ACCOUNTS_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_provider_accounts_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateModifiedByUserErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
