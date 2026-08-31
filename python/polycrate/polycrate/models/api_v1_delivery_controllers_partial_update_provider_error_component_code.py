from typing import Literal

ApiV1DeliveryControllersPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_delivery_controllers_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateProviderErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
