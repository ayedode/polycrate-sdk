from typing import Literal

ApiV1PolicyBindingsCreateExecutionLogErrorComponentAttr = Literal["execution_log"]

API_V1_POLICY_BINDINGS_CREATE_EXECUTION_LOG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsCreateExecutionLogErrorComponentAttr
] = {
    "execution_log",
}


def check_api_v1_policy_bindings_create_execution_log_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsCreateExecutionLogErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_CREATE_EXECUTION_LOG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_CREATE_EXECUTION_LOG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
