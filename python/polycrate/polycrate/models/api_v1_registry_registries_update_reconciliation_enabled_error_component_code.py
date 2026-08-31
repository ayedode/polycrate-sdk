from typing import Literal

ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_REGISTRY_REGISTRIES_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_registry_registries_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
