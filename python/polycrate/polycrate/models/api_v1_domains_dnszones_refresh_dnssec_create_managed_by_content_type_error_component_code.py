from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type"
]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_managed_by_content_type_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
