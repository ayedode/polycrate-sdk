from typing import Literal

ApiV1DeliveryControllersPartialUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_delivery_controllers_partial_update_metadata_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateMetadataErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
