from typing import Literal

ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_provider_accounts_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
