from typing import Literal

ApiV1DomainsDomainsUpdateExpiryDateErrorComponentAttr = Literal["expiry_date"]

API_V1_DOMAINS_DOMAINS_UPDATE_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateExpiryDateErrorComponentAttr
] = {
    "expiry_date",
}


def check_api_v1_domains_domains_update_expiry_date_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateExpiryDateErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
