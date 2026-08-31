from typing import Literal

ApiV1DeliveryControllersPartialUpdateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_delivery_controllers_partial_update_metadata_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateMetadataErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
