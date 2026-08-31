from typing import Literal

ApiV1DomainsDomainsCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_DOMAINS_DOMAINS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_domains_domains_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateSlaTargetErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
