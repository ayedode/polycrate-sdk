from typing import Literal

ApiV1DomainsDomainsCreateExpiryDateErrorComponentAttr = Literal["expiry_date"]

API_V1_DOMAINS_DOMAINS_CREATE_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateExpiryDateErrorComponentAttr
] = {
    "expiry_date",
}


def check_api_v1_domains_domains_create_expiry_date_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateExpiryDateErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
