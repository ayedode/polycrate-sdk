from typing import Literal

ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_assistant_sessions_messages_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
