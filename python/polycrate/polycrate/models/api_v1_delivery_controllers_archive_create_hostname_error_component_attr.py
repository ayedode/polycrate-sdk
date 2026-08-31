from typing import Literal

ApiV1DeliveryControllersArchiveCreateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_delivery_controllers_archive_create_hostname_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateHostnameErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
