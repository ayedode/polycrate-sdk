from typing import Literal

ApiV1BlocksReconcileCreateSupportsHaErrorComponentAttr = Literal["supports_ha"]

API_V1_BLOCKS_RECONCILE_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateSupportsHaErrorComponentAttr
] = {
    "supports_ha",
}


def check_api_v1_blocks_reconcile_create_supports_ha_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateSupportsHaErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
