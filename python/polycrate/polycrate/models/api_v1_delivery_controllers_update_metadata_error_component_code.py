from typing import Literal

ApiV1DeliveryControllersUpdateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersUpdateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_delivery_controllers_update_metadata_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersUpdateMetadataErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
