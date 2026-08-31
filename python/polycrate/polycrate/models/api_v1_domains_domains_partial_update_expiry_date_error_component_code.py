from typing import Literal

ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_EXPIRY_DATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_domains_domains_partial_update_expiry_date_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_EXPIRY_DATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_EXPIRY_DATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
