from typing import Literal

ApiV1DeliveryControllersCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DELIVERY_CONTROLLERS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_delivery_controllers_create_criticality_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateCriticalityErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
