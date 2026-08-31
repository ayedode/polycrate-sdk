from typing import Literal

ApiV1DeliveryControllersCreateControllerAppVersionErrorComponentAttr = Literal["controller_app_version"]

API_V1_DELIVERY_CONTROLLERS_CREATE_CONTROLLER_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateControllerAppVersionErrorComponentAttr
] = {
    "controller_app_version",
}


def check_api_v1_delivery_controllers_create_controller_app_version_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateControllerAppVersionErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_CONTROLLER_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_CONTROLLER_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
