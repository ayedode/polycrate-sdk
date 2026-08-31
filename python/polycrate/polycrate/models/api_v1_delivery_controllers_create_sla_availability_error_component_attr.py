from typing import Literal

ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_DELIVERY_CONTROLLERS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_delivery_controllers_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
