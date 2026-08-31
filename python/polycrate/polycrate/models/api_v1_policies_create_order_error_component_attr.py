from typing import Literal

ApiV1PoliciesCreateOrderErrorComponentAttr = Literal["order"]

API_V1_POLICIES_CREATE_ORDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesCreateOrderErrorComponentAttr] = {
    "order",
}


def check_api_v1_policies_create_order_error_component_attr(value: str) -> ApiV1PoliciesCreateOrderErrorComponentAttr:
    if value in API_V1_POLICIES_CREATE_ORDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_ORDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
