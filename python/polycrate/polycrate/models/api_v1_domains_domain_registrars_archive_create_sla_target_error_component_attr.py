from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_domains_domain_registrars_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
