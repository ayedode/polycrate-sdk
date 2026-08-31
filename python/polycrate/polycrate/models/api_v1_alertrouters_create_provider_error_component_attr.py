from typing import Literal

ApiV1AlertroutersCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTROUTERS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_alertrouters_create_provider_error_component_attr(
    value: str,
) -> ApiV1AlertroutersCreateProviderErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
