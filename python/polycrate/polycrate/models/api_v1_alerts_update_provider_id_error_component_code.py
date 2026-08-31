from typing import Literal

ApiV1AlertsUpdateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateProviderIdErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_update_provider_id_error_component_code(
    value: str,
) -> ApiV1AlertsUpdateProviderIdErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
