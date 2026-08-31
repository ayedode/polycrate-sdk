from typing import Literal

ApiV1ProviderAccountsCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PROVIDER_ACCOUNTS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_provider_accounts_create_display_name_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateDisplayNameErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
