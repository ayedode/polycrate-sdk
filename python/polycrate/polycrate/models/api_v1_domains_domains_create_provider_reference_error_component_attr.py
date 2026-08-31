from typing import Literal

ApiV1DomainsDomainsCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_DOMAINS_DOMAINS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_domains_domains_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
