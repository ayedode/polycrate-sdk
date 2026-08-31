from typing import Literal

ApiV1AssistantSessionsCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_ASSISTANT_SESSIONS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_assistant_sessions_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsCreateSlaTargetErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
