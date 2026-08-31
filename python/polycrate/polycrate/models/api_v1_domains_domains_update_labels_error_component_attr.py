from typing import Literal

ApiV1DomainsDomainsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DOMAINS_DOMAINS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_domains_domains_update_labels_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateLabelsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
