from typing import Literal

ApiV1DomainsDnszonesListStateErrorComponentAttr = Literal["state"]

API_V1_DOMAINS_DNSZONES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DomainsDnszonesListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_domains_dnszones_list_state_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesListStateErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
