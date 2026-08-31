from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_domains_domain_registrars_archive_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
