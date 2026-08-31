from typing import Literal

ApiV1AlertsDiscoverCreateNamespaceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_DISCOVER_CREATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsDiscoverCreateNamespaceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_discover_create_namespace_error_component_code(
    value: str,
) -> ApiV1AlertsDiscoverCreateNamespaceErrorComponentCode:
    if value in API_V1_ALERTS_DISCOVER_CREATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
