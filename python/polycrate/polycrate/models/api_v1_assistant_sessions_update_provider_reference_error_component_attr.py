from typing import Literal

ApiV1AssistantSessionsUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_ASSISTANT_SESSIONS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_assistant_sessions_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
