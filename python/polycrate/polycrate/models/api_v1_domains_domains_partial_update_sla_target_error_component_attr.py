from typing import Literal

ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_domains_domains_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
