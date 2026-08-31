from typing import Literal

ApiV1PoliciesCreateExpressionErrorComponentAttr = Literal["expression"]

API_V1_POLICIES_CREATE_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesCreateExpressionErrorComponentAttr] = {
    "expression",
}


def check_api_v1_policies_create_expression_error_component_attr(
    value: str,
) -> ApiV1PoliciesCreateExpressionErrorComponentAttr:
    if value in API_V1_POLICIES_CREATE_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
