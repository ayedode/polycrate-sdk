from typing import Literal

ApiV1DeliveryControllersUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_delivery_controllers_update_provider_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersUpdateProviderErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
