from typing import Literal

ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_delivery_controllers_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
