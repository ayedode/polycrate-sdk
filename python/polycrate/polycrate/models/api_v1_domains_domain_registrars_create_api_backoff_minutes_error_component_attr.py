from typing import Literal

ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponentAttr = Literal["api_backoff_minutes"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponentAttr
] = {
    "api_backoff_minutes",
}


def check_api_v1_domains_domain_registrars_create_api_backoff_minutes_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
