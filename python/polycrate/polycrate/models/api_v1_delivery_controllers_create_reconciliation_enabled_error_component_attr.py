from typing import Literal

ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_DELIVERY_CONTROLLERS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_delivery_controllers_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
