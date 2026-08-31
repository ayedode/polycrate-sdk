from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_domains_domain_registrars_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
