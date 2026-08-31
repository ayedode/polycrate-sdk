from typing import Literal

ApiV1DomainsDnszonesListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_DOMAINS_DNSZONES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesListSearchErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_domains_dnszones_list_search_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesListSearchErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
