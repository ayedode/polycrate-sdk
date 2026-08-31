from typing import Literal

ApiV1DomainsDnszonesListKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DNSZONES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DomainsDnszonesListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_domains_dnszones_list_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesListKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
