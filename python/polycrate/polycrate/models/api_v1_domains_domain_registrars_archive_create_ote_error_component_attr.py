from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponentAttr = Literal["ote"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_OTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponentAttr
] = {
    "ote",
}


def check_api_v1_domains_domain_registrars_archive_create_ote_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_OTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_OTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
