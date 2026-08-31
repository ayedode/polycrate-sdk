from typing import Literal

ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_provider_accounts_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
