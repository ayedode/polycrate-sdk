from typing import Literal

ApiV1DeliveryControllersPartialUpdateCredentialErrorComponentAttr = Literal["credential"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_delivery_controllers_partial_update_credential_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateCredentialErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
