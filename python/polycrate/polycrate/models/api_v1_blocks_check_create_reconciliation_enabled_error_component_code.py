from typing import Literal

ApiV1BlocksCheckCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_CHECK_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_check_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
