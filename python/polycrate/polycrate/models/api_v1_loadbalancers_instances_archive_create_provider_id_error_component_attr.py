from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_loadbalancers_instances_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
