from typing import Literal

ApiV1DeliveryControllersUpdateCredentialErrorComponentAttr = Literal["credential"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersUpdateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_delivery_controllers_update_credential_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersUpdateCredentialErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
