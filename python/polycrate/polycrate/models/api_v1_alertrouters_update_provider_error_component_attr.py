from typing import Literal

ApiV1AlertroutersUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTROUTERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_alertrouters_update_provider_error_component_attr(
    value: str,
) -> ApiV1AlertroutersUpdateProviderErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
