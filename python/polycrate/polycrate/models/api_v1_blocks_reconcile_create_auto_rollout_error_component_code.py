from typing import Literal

ApiV1BlocksReconcileCreateAutoRolloutErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_RECONCILE_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksReconcileCreateAutoRolloutErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_reconcile_create_auto_rollout_error_component_code(
    value: str,
) -> ApiV1BlocksReconcileCreateAutoRolloutErrorComponentCode:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
