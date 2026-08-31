from typing import Literal

ApiV1ProviderAccountsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_provider_accounts_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
