from typing import Literal

ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_delivery_controllers_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
