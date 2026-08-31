from typing import Literal

ApiV1PoliciesPartialUpdateOrderErrorComponentAttr = Literal["order"]

API_V1_POLICIES_PARTIAL_UPDATE_ORDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesPartialUpdateOrderErrorComponentAttr
] = {
    "order",
}


def check_api_v1_policies_partial_update_order_error_component_attr(
    value: str,
) -> ApiV1PoliciesPartialUpdateOrderErrorComponentAttr:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_ORDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_ORDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
