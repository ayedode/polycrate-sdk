from typing import Literal

ApiV1PolicyBindingsPartialUpdatePolicyIdErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_POLICY_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsPartialUpdatePolicyIdErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_policy_bindings_partial_update_policy_id_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsPartialUpdatePolicyIdErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_POLICY_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_POLICY_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
