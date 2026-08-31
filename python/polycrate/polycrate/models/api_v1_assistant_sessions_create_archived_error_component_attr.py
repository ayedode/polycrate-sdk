from typing import Literal

ApiV1AssistantSessionsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ASSISTANT_SESSIONS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_assistant_sessions_create_archived_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsCreateArchivedErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
