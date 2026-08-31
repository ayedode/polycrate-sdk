from typing import Literal

ApiV1DeliveryControllersUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_delivery_controllers_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersUpdateSloTargetErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
