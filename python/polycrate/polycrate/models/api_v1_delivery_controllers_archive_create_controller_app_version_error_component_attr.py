from typing import Literal

ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponentAttr = Literal["controller_app_version"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_CONTROLLER_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponentAttr
] = {
    "controller_app_version",
}


def check_api_v1_delivery_controllers_archive_create_controller_app_version_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateControllerAppVersionErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_CONTROLLER_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_CONTROLLER_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
