from typing import Literal

ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_assistant_sessions_archive_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsArchiveCreateSloTargetErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
