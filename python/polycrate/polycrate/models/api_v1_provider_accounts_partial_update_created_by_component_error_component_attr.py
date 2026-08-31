from typing import Literal

ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_provider_accounts_partial_update_created_by_component_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
