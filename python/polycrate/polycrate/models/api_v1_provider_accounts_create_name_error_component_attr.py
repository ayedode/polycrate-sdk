from typing import Literal

ApiV1ProviderAccountsCreateNameErrorComponentAttr = Literal["name"]

API_V1_PROVIDER_ACCOUNTS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_provider_accounts_create_name_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateNameErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
