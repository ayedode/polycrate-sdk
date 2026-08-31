from typing import Literal

ApiV1ProviderAccountsCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_PROVIDER_ACCOUNTS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_provider_accounts_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
