from typing import Literal

ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_DELIVERY_CONTROLLERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_delivery_controllers_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
