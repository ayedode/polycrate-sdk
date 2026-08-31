from typing import Literal

ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_assistant_sessions_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
