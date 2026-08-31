from typing import Literal

ApiV1ProvidersCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PROVIDERS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersCreateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_providers_create_provider_error_component_attr(
    value: str,
) -> ApiV1ProvidersCreateProviderErrorComponentAttr:
    if value in API_V1_PROVIDERS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
