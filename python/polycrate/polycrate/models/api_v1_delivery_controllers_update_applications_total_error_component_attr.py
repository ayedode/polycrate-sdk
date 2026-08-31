from typing import Literal

ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponentAttr = Literal["applications_total"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_TOTAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponentAttr
] = {
    "applications_total",
}


def check_api_v1_delivery_controllers_update_applications_total_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersUpdateApplicationsTotalErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_TOTAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_TOTAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
