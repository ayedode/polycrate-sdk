from typing import Literal

ApiV1PoliciesUpdateOrderErrorComponentCode = Literal["invalid", "max_string_length", "max_value", "min_value", "null"]

API_V1_POLICIES_UPDATE_ORDER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PoliciesUpdateOrderErrorComponentCode] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_policies_update_order_error_component_code(value: str) -> ApiV1PoliciesUpdateOrderErrorComponentCode:
    if value in API_V1_POLICIES_UPDATE_ORDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_ORDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
