from typing import Literal

ApiV1PolicyBindingsPartialUpdateAppliedErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_APPLIED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsPartialUpdateAppliedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policy_bindings_partial_update_applied_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsPartialUpdateAppliedErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_APPLIED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_APPLIED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
