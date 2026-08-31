from typing import Literal

ApiV1AssistantSessionsUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_ASSISTANT_SESSIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_assistant_sessions_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
