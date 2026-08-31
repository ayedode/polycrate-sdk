from typing import Literal

ApiV1DeliveryControllersCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_DELIVERY_CONTROLLERS_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_delivery_controllers_create_metadata_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateMetadataErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
