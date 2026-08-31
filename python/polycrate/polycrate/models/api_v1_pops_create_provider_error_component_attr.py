from typing import Literal

ApiV1PopsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_POPS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsCreateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_pops_create_provider_error_component_attr(value: str) -> ApiV1PopsCreateProviderErrorComponentAttr:
    if value in API_V1_POPS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
