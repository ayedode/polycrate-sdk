from typing import Literal

ApiV1AlertsReconcileCreateBlockErrorComponentAttr = Literal["block"]

API_V1_ALERTS_RECONCILE_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateBlockErrorComponentAttr
] = {
    "block",
}


def check_api_v1_alerts_reconcile_create_block_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateBlockErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
