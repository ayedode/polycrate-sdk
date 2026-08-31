from typing import Literal

ApiV1PoliciesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_POLICIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesCreateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_policies_create_provider_error_component_attr(
    value: str,
) -> ApiV1PoliciesCreateProviderErrorComponentAttr:
    if value in API_V1_POLICIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
