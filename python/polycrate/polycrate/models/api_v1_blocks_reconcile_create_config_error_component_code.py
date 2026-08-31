from typing import Literal

ApiV1BlocksReconcileCreateConfigErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_RECONCILE_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksReconcileCreateConfigErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_reconcile_create_config_error_component_code(
    value: str,
) -> ApiV1BlocksReconcileCreateConfigErrorComponentCode:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
