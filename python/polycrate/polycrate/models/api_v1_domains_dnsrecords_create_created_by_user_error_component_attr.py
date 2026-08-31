from typing import Literal

ApiV1DomainsDnsrecordsCreateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

API_V1_DOMAINS_DNSRECORDS_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsCreateCreatedByUserErrorComponentAttr
] = {
    "created_by_user",
}


def check_api_v1_domains_dnsrecords_create_created_by_user_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateCreatedByUserErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
