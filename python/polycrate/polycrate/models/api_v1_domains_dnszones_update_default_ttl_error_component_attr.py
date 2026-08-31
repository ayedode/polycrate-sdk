from typing import Literal

ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponentAttr = Literal["default_ttl"]

API_V1_DOMAINS_DNSZONES_UPDATE_DEFAULT_TTL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponentAttr
] = {
    "default_ttl",
}


def check_api_v1_domains_dnszones_update_default_ttl_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_DEFAULT_TTL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_DEFAULT_TTL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
