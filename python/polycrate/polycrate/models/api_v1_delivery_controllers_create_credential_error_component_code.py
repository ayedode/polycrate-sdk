from typing import Literal

ApiV1DeliveryControllersCreateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DELIVERY_CONTROLLERS_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersCreateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_delivery_controllers_create_credential_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersCreateCredentialErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
