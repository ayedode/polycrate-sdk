from typing import Literal

ApiV1DeliveryControllersArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_delivery_controllers_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateNameErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
