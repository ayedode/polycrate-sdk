from typing import Literal

ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponentAttr = Literal["consumer_meta"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_CONSUMER_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponentAttr
] = {
    "consumer_meta",
}


def check_api_v1_loadbalancers_instances_create_consumer_meta_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateConsumerMetaErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_CONSUMER_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_CONSUMER_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
