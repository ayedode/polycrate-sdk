from typing import Literal

ApiV1DeliveryControllersUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_delivery_controllers_update_display_name_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
