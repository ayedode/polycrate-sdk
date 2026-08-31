from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_domain_registrars_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
