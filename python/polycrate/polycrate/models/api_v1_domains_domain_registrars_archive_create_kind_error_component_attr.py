from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_domain_registrars_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
