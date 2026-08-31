from typing import Literal

ApiV1AssistantSessionsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ASSISTANT_SESSIONS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_assistant_sessions_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsCreateTolerationsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
