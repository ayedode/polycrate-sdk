from typing import Literal

ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_CREDENTIALS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_credentials_reconcile_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
