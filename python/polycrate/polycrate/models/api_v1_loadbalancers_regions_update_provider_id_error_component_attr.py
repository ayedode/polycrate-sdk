from typing import Literal

ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_loadbalancers_regions_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateProviderIdErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
