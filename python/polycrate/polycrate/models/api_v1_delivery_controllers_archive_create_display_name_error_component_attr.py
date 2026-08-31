from typing import Literal

ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_delivery_controllers_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
