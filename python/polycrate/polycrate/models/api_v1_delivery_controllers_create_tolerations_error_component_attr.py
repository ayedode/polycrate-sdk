from typing import Literal

ApiV1DeliveryControllersCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DELIVERY_CONTROLLERS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_delivery_controllers_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateTolerationsErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
