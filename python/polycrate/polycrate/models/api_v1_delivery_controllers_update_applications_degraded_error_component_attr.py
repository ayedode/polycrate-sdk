from typing import Literal

ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponentAttr = Literal["applications_degraded"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_DEGRADED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponentAttr
] = {
    "applications_degraded",
}


def check_api_v1_delivery_controllers_update_applications_degraded_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_DEGRADED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_DEGRADED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
