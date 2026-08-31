from typing import Literal

ApiV1DeliveryControllersUpdateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersUpdateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_delivery_controllers_update_credential_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersUpdateCredentialErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
