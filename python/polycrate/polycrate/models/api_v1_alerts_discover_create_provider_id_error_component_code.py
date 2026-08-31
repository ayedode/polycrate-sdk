from typing import Literal

ApiV1AlertsDiscoverCreateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_DISCOVER_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsDiscoverCreateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_discover_create_provider_id_error_component_code(
    value: str,
) -> ApiV1AlertsDiscoverCreateProviderIdErrorComponentCode:
    if value in API_V1_ALERTS_DISCOVER_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
