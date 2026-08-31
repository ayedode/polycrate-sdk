from typing import Literal

ApiV1ProviderAccountsCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PROVIDER_ACCOUNTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_provider_accounts_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
