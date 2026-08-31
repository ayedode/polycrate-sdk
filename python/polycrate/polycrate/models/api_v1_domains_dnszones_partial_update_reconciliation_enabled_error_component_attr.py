from typing import Literal

ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_domains_dnszones_partial_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
