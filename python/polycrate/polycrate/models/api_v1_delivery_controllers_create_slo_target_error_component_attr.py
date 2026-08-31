from typing import Literal

ApiV1DeliveryControllersCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_DELIVERY_CONTROLLERS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_delivery_controllers_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateSloTargetErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
