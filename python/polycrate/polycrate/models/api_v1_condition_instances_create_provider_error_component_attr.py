from typing import Literal

ApiV1ConditionInstancesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_CONDITION_INSTANCES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_condition_instances_create_provider_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateProviderErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
