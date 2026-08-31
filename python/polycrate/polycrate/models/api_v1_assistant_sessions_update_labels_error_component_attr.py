from typing import Literal

ApiV1AssistantSessionsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ASSISTANT_SESSIONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_assistant_sessions_update_labels_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsUpdateLabelsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
