from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponentCode = Literal["invalid"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_CONSUMER_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_loadbalancers_instances_archive_create_consumer_meta_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_CONSUMER_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_CONSUMER_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
