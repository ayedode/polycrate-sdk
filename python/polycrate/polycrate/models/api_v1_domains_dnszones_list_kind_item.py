from typing import Literal

ApiV1DomainsDnszonesListKindItem = Literal["external", "internal"]

API_V1_DOMAINS_DNSZONES_LIST_KIND_ITEM_VALUES: set[ApiV1DomainsDnszonesListKindItem] = {
    "external",
    "internal",
}


def check_api_v1_domains_dnszones_list_kind_item(value: str) -> ApiV1DomainsDnszonesListKindItem:
    if value in API_V1_DOMAINS_DNSZONES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_KIND_ITEM_VALUES!r}")
