from typing import Literal

ApiV1PoliciesPartialUpdateExpressionErrorComponentAttr = Literal["expression"]

API_V1_POLICIES_PARTIAL_UPDATE_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesPartialUpdateExpressionErrorComponentAttr
] = {
    "expression",
}


def check_api_v1_policies_partial_update_expression_error_component_attr(
    value: str,
) -> ApiV1PoliciesPartialUpdateExpressionErrorComponentAttr:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
