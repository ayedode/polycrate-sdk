from typing import Literal

ApiV1DeliveryControllersCreateApplicationsTotalErrorComponentAttr = Literal["applications_total"]

API_V1_DELIVERY_CONTROLLERS_CREATE_APPLICATIONS_TOTAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateApplicationsTotalErrorComponentAttr
] = {
    "applications_total",
}


def check_api_v1_delivery_controllers_create_applications_total_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateApplicationsTotalErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_APPLICATIONS_TOTAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_APPLICATIONS_TOTAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
