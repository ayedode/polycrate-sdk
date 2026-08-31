from typing import Literal

ApiV1DomainsDnszonesListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_DOMAINS_DNSZONES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_domains_dnszones_list_state_not_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesListStateNotErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
