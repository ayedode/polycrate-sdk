from typing import Literal

ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_DELIVERY_CONTROLLERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_delivery_controllers_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
