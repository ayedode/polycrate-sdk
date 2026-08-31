from typing import Literal

ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_secretmanager_managers_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
