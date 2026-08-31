from typing import Literal

ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_condition_instances_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
