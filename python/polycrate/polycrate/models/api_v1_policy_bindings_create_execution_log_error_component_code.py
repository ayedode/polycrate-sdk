from typing import Literal

ApiV1PolicyBindingsCreateExecutionLogErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICY_BINDINGS_CREATE_EXECUTION_LOG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsCreateExecutionLogErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policy_bindings_create_execution_log_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsCreateExecutionLogErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_CREATE_EXECUTION_LOG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_CREATE_EXECUTION_LOG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
