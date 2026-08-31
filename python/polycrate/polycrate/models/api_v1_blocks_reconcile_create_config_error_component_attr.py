from typing import Literal

ApiV1BlocksReconcileCreateConfigErrorComponentAttr = Literal["config"]

API_V1_BLOCKS_RECONCILE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_blocks_reconcile_create_config_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateConfigErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
