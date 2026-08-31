from typing import Literal

ApiV1AlertsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_alerts_create_provider_error_component_attr(value: str) -> ApiV1AlertsCreateProviderErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
