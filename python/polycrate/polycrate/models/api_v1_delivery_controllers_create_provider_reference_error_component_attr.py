from typing import Literal

ApiV1DeliveryControllersCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_DELIVERY_CONTROLLERS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_delivery_controllers_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
