from typing import Literal

ApiV1AssistantSessionsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ASSISTANT_SESSIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_assistant_sessions_update_archived_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsUpdateArchivedErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
