from typing import Literal

ApiV1AlertsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_alerts_update_provider_error_component_attr(value: str) -> ApiV1AlertsUpdateProviderErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
