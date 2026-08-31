from typing import Literal

ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponentAttr = Literal["object_id"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponentAttr
] = {
    "object_id",
}


def check_api_v1_condition_instances_archive_create_object_id_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
