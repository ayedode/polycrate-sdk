from typing import Literal

ApiV1PrefixesUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_PREFIXES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesUpdateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_prefixes_update_provider_error_component_attr(
    value: str,
) -> ApiV1PrefixesUpdateProviderErrorComponentAttr:
    if value in API_V1_PREFIXES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
