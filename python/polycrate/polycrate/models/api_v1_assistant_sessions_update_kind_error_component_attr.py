from typing import Literal

ApiV1AssistantSessionsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_ASSISTANT_SESSIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_assistant_sessions_update_kind_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsUpdateKindErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
