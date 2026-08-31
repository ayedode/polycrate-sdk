from typing import Literal

ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_delivery_controllers_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
