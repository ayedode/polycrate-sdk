from typing import Literal

ApiV1DomainsDnszonesRectifyCreateKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_dnszones_rectify_create_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
