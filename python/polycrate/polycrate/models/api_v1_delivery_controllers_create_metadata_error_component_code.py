from typing import Literal

ApiV1DeliveryControllersCreateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_DELIVERY_CONTROLLERS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersCreateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_delivery_controllers_create_metadata_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersCreateMetadataErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
