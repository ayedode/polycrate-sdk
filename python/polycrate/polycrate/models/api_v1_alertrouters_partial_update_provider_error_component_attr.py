from typing import Literal

ApiV1AlertroutersPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_alertrouters_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1AlertroutersPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
