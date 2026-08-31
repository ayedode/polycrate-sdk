from typing import Literal

ApiV1AlertsUpdateNamespaceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_UPDATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateNamespaceErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_update_namespace_error_component_code(
    value: str,
) -> ApiV1AlertsUpdateNamespaceErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
