from typing import Literal

ApiV1PolicyBindingsPartialUpdateExecutionLogErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_EXECUTION_LOG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsPartialUpdateExecutionLogErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policy_bindings_partial_update_execution_log_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsPartialUpdateExecutionLogErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_EXECUTION_LOG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_EXECUTION_LOG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
