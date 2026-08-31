from typing import Literal

ApiV1DomainsDnszonesListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_DOMAINS_DNSZONES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_domains_dnszones_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesListUpdatedAtErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
