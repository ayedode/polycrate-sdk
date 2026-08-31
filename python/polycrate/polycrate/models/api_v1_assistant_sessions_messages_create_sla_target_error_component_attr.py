from typing import Literal

ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_assistant_sessions_messages_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
