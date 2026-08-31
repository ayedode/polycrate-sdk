from typing import Literal

ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_assistant_sessions_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
