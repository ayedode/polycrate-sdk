from typing import Literal

ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_run_discovery_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
