from typing import Literal

ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_delivery_controllers_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
