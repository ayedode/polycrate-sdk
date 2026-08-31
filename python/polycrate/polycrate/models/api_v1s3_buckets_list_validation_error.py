from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1s3_buckets_list_created_at_error_component import ApiV1S3BucketsListCreatedAtErrorComponent
    from ..models.api_v1s3_buckets_list_created_by_component_error_component import (
        ApiV1S3BucketsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1s3_buckets_list_created_by_users_error_component import (
        ApiV1S3BucketsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1s3_buckets_list_kind_error_component import ApiV1S3BucketsListKindErrorComponent
    from ..models.api_v1s3_buckets_list_name_error_component import ApiV1S3BucketsListNameErrorComponent
    from ..models.api_v1s3_buckets_list_name_exact_error_component import ApiV1S3BucketsListNameExactErrorComponent
    from ..models.api_v1s3_buckets_list_organizations_error_component import (
        ApiV1S3BucketsListOrganizationsErrorComponent,
    )
    from ..models.api_v1s3_buckets_list_region_error_component import ApiV1S3BucketsListRegionErrorComponent
    from ..models.api_v1s3_buckets_list_s3_cluster_error_component import ApiV1S3BucketsListS3ClusterErrorComponent
    from ..models.api_v1s3_buckets_list_scope_error_component import ApiV1S3BucketsListScopeErrorComponent
    from ..models.api_v1s3_buckets_list_search_error_component import ApiV1S3BucketsListSearchErrorComponent
    from ..models.api_v1s3_buckets_list_state_error_component import ApiV1S3BucketsListStateErrorComponent
    from ..models.api_v1s3_buckets_list_state_not_error_component import ApiV1S3BucketsListStateNotErrorComponent
    from ..models.api_v1s3_buckets_list_storage_class_error_component import (
        ApiV1S3BucketsListStorageClassErrorComponent,
    )
    from ..models.api_v1s3_buckets_list_time_range_error_component import ApiV1S3BucketsListTimeRangeErrorComponent
    from ..models.api_v1s3_buckets_list_updated_at_error_component import ApiV1S3BucketsListUpdatedAtErrorComponent
    from ..models.api_v1s3_buckets_list_workspaces_error_component import ApiV1S3BucketsListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1S3BucketsListValidationError")


@_attrs_define
class ApiV1S3BucketsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1S3BucketsListCreatedAtErrorComponent | ApiV1S3BucketsListCreatedByComponentErrorComponent |
            ApiV1S3BucketsListCreatedByUsersErrorComponent | ApiV1S3BucketsListKindErrorComponent |
            ApiV1S3BucketsListNameErrorComponent | ApiV1S3BucketsListNameExactErrorComponent |
            ApiV1S3BucketsListOrganizationsErrorComponent | ApiV1S3BucketsListRegionErrorComponent |
            ApiV1S3BucketsListS3ClusterErrorComponent | ApiV1S3BucketsListScopeErrorComponent |
            ApiV1S3BucketsListSearchErrorComponent | ApiV1S3BucketsListStateErrorComponent |
            ApiV1S3BucketsListStateNotErrorComponent | ApiV1S3BucketsListStorageClassErrorComponent |
            ApiV1S3BucketsListTimeRangeErrorComponent | ApiV1S3BucketsListUpdatedAtErrorComponent |
            ApiV1S3BucketsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1S3BucketsListCreatedAtErrorComponent
        | ApiV1S3BucketsListCreatedByComponentErrorComponent
        | ApiV1S3BucketsListCreatedByUsersErrorComponent
        | ApiV1S3BucketsListKindErrorComponent
        | ApiV1S3BucketsListNameErrorComponent
        | ApiV1S3BucketsListNameExactErrorComponent
        | ApiV1S3BucketsListOrganizationsErrorComponent
        | ApiV1S3BucketsListRegionErrorComponent
        | ApiV1S3BucketsListS3ClusterErrorComponent
        | ApiV1S3BucketsListScopeErrorComponent
        | ApiV1S3BucketsListSearchErrorComponent
        | ApiV1S3BucketsListStateErrorComponent
        | ApiV1S3BucketsListStateNotErrorComponent
        | ApiV1S3BucketsListStorageClassErrorComponent
        | ApiV1S3BucketsListTimeRangeErrorComponent
        | ApiV1S3BucketsListUpdatedAtErrorComponent
        | ApiV1S3BucketsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1s3_buckets_list_created_at_error_component import ApiV1S3BucketsListCreatedAtErrorComponent
        from ..models.api_v1s3_buckets_list_created_by_component_error_component import (
            ApiV1S3BucketsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1s3_buckets_list_created_by_users_error_component import (
            ApiV1S3BucketsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1s3_buckets_list_kind_error_component import ApiV1S3BucketsListKindErrorComponent
        from ..models.api_v1s3_buckets_list_name_error_component import ApiV1S3BucketsListNameErrorComponent
        from ..models.api_v1s3_buckets_list_organizations_error_component import (
            ApiV1S3BucketsListOrganizationsErrorComponent,
        )
        from ..models.api_v1s3_buckets_list_region_error_component import ApiV1S3BucketsListRegionErrorComponent
        from ..models.api_v1s3_buckets_list_s3_cluster_error_component import ApiV1S3BucketsListS3ClusterErrorComponent
        from ..models.api_v1s3_buckets_list_scope_error_component import ApiV1S3BucketsListScopeErrorComponent
        from ..models.api_v1s3_buckets_list_search_error_component import ApiV1S3BucketsListSearchErrorComponent
        from ..models.api_v1s3_buckets_list_state_error_component import ApiV1S3BucketsListStateErrorComponent
        from ..models.api_v1s3_buckets_list_state_not_error_component import ApiV1S3BucketsListStateNotErrorComponent
        from ..models.api_v1s3_buckets_list_storage_class_error_component import (
            ApiV1S3BucketsListStorageClassErrorComponent,
        )
        from ..models.api_v1s3_buckets_list_time_range_error_component import ApiV1S3BucketsListTimeRangeErrorComponent
        from ..models.api_v1s3_buckets_list_updated_at_error_component import ApiV1S3BucketsListUpdatedAtErrorComponent
        from ..models.api_v1s3_buckets_list_workspaces_error_component import ApiV1S3BucketsListWorkspacesErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1S3BucketsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListS3ClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1s3_buckets_list_created_at_error_component import ApiV1S3BucketsListCreatedAtErrorComponent
        from ..models.api_v1s3_buckets_list_created_by_component_error_component import (
            ApiV1S3BucketsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1s3_buckets_list_created_by_users_error_component import (
            ApiV1S3BucketsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1s3_buckets_list_kind_error_component import ApiV1S3BucketsListKindErrorComponent
        from ..models.api_v1s3_buckets_list_name_error_component import ApiV1S3BucketsListNameErrorComponent
        from ..models.api_v1s3_buckets_list_name_exact_error_component import ApiV1S3BucketsListNameExactErrorComponent
        from ..models.api_v1s3_buckets_list_organizations_error_component import (
            ApiV1S3BucketsListOrganizationsErrorComponent,
        )
        from ..models.api_v1s3_buckets_list_region_error_component import ApiV1S3BucketsListRegionErrorComponent
        from ..models.api_v1s3_buckets_list_s3_cluster_error_component import ApiV1S3BucketsListS3ClusterErrorComponent
        from ..models.api_v1s3_buckets_list_scope_error_component import ApiV1S3BucketsListScopeErrorComponent
        from ..models.api_v1s3_buckets_list_search_error_component import ApiV1S3BucketsListSearchErrorComponent
        from ..models.api_v1s3_buckets_list_state_error_component import ApiV1S3BucketsListStateErrorComponent
        from ..models.api_v1s3_buckets_list_state_not_error_component import ApiV1S3BucketsListStateNotErrorComponent
        from ..models.api_v1s3_buckets_list_storage_class_error_component import (
            ApiV1S3BucketsListStorageClassErrorComponent,
        )
        from ..models.api_v1s3_buckets_list_time_range_error_component import ApiV1S3BucketsListTimeRangeErrorComponent
        from ..models.api_v1s3_buckets_list_updated_at_error_component import ApiV1S3BucketsListUpdatedAtErrorComponent
        from ..models.api_v1s3_buckets_list_workspaces_error_component import ApiV1S3BucketsListWorkspacesErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1S3BucketsListCreatedAtErrorComponent
                | ApiV1S3BucketsListCreatedByComponentErrorComponent
                | ApiV1S3BucketsListCreatedByUsersErrorComponent
                | ApiV1S3BucketsListKindErrorComponent
                | ApiV1S3BucketsListNameErrorComponent
                | ApiV1S3BucketsListNameExactErrorComponent
                | ApiV1S3BucketsListOrganizationsErrorComponent
                | ApiV1S3BucketsListRegionErrorComponent
                | ApiV1S3BucketsListS3ClusterErrorComponent
                | ApiV1S3BucketsListScopeErrorComponent
                | ApiV1S3BucketsListSearchErrorComponent
                | ApiV1S3BucketsListStateErrorComponent
                | ApiV1S3BucketsListStateNotErrorComponent
                | ApiV1S3BucketsListStorageClassErrorComponent
                | ApiV1S3BucketsListTimeRangeErrorComponent
                | ApiV1S3BucketsListUpdatedAtErrorComponent
                | ApiV1S3BucketsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_0 = (
                        ApiV1S3BucketsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_1 = (
                        ApiV1S3BucketsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_2 = (
                        ApiV1S3BucketsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_3 = (
                        ApiV1S3BucketsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_4 = (
                        ApiV1S3BucketsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_5 = (
                        ApiV1S3BucketsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_6 = (
                        ApiV1S3BucketsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_7 = (
                        ApiV1S3BucketsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_8 = (
                        ApiV1S3BucketsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_9 = (
                        ApiV1S3BucketsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_10 = (
                        ApiV1S3BucketsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_11 = (
                        ApiV1S3BucketsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_12 = (
                        ApiV1S3BucketsListS3ClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_13 = (
                        ApiV1S3BucketsListRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_14 = (
                        ApiV1S3BucketsListStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_list_error_type_15 = (
                        ApiV1S3BucketsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1s3_buckets_list_error_type_16 = (
                    ApiV1S3BucketsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1s3_buckets_list_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1s3_buckets_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1s3_buckets_list_validation_error.additional_properties = d
        return api_v1s3_buckets_list_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
