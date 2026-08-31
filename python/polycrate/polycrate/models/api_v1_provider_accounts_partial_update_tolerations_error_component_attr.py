from typing import Literal

ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_provider_accounts_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
