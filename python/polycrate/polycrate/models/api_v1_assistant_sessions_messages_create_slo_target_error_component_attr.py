from typing import Literal

ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_assistant_sessions_messages_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
