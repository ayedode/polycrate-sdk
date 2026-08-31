from typing import Literal

ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_delivery_controllers_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
