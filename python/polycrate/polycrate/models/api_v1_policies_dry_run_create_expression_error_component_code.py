from typing import Literal

ApiV1PoliciesDryRunCreateExpressionErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_POLICIES_DRY_RUN_CREATE_EXPRESSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateExpressionErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_policies_dry_run_create_expression_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateExpressionErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_EXPRESSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_EXPRESSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
