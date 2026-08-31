from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_dnsrecords_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
