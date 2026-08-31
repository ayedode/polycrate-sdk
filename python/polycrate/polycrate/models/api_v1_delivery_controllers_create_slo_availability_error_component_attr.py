from typing import Literal

ApiV1DeliveryControllersCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_DELIVERY_CONTROLLERS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_delivery_controllers_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
