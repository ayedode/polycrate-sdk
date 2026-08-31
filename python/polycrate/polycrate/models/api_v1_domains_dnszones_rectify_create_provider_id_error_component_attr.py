from typing import Literal

ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_domains_dnszones_rectify_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
