from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_loadbalancers_regions_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
