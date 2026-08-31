from typing import Literal

ApiV1PoliciesPartialUpdateExpressionErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_POLICIES_PARTIAL_UPDATE_EXPRESSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesPartialUpdateExpressionErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_policies_partial_update_expression_error_component_code(
    value: str,
) -> ApiV1PoliciesPartialUpdateExpressionErrorComponentCode:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_EXPRESSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_EXPRESSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
