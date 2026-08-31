from typing import Literal

ApiV1DeliveryControllersCreateNameErrorComponentAttr = Literal["name"]

API_V1_DELIVERY_CONTROLLERS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_delivery_controllers_create_name_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateNameErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
