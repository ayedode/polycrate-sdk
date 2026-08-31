from typing import Literal

ApiV1DeliveryControllersCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DELIVERY_CONTROLLERS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_delivery_controllers_create_provider_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersCreateProviderErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
