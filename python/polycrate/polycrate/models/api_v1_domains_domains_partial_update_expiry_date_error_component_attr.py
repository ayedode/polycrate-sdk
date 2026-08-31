from typing import Literal

ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponentAttr = Literal["expiry_date"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponentAttr
] = {
    "expiry_date",
}


def check_api_v1_domains_domains_partial_update_expiry_date_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
