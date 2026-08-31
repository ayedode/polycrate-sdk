from typing import Literal

ApiV1DomainsDnszonesPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_dnszones_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
