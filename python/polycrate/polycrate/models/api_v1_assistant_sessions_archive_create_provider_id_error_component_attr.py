from typing import Literal

ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_assistant_sessions_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
