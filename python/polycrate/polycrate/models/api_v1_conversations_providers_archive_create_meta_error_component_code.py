from typing import Literal

ApiV1ConversationsProvidersArchiveCreateMetaErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_CONVERSATIONS_PROVIDERS_ARCHIVE_CREATE_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsProvidersArchiveCreateMetaErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_conversations_providers_archive_create_meta_error_component_code(
    value: str,
) -> ApiV1ConversationsProvidersArchiveCreateMetaErrorComponentCode:
    if value in API_V1_CONVERSATIONS_PROVIDERS_ARCHIVE_CREATE_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_ARCHIVE_CREATE_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
