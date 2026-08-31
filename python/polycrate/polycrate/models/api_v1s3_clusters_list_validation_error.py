from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1s3_clusters_list_created_at_error_component import ApiV1S3ClustersListCreatedAtErrorComponent
    from ..models.api_v1s3_clusters_list_created_by_component_error_component import (
        ApiV1S3ClustersListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1s3_clusters_list_created_by_users_error_component import (
        ApiV1S3ClustersListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1s3_clusters_list_kind_error_component import ApiV1S3ClustersListKindErrorComponent
    from ..models.api_v1s3_clusters_list_name_error_component import ApiV1S3ClustersListNameErrorComponent
    from ..models.api_v1s3_clusters_list_name_exact_error_component import ApiV1S3ClustersListNameExactErrorComponent
    from ..models.api_v1s3_clusters_list_organizations_error_component import (
        ApiV1S3ClustersListOrganizationsErrorComponent,
    )
    from ..models.api_v1s3_clusters_list_region_error_component import ApiV1S3ClustersListRegionErrorComponent
    from ..models.api_v1s3_clusters_list_scope_error_component import ApiV1S3ClustersListScopeErrorComponent
    from ..models.api_v1s3_clusters_list_search_error_component import ApiV1S3ClustersListSearchErrorComponent
    from ..models.api_v1s3_clusters_list_state_error_component import ApiV1S3ClustersListStateErrorComponent
    from ..models.api_v1s3_clusters_list_state_not_error_component import ApiV1S3ClustersListStateNotErrorComponent
    from ..models.api_v1s3_clusters_list_time_range_error_component import ApiV1S3ClustersListTimeRangeErrorComponent
    from ..models.api_v1s3_clusters_list_updated_at_error_component import ApiV1S3ClustersListUpdatedAtErrorComponent
    from ..models.api_v1s3_clusters_list_workspaces_error_component import ApiV1S3ClustersListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1S3ClustersListValidationError")


@_attrs_define
class ApiV1S3ClustersListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1S3ClustersListCreatedAtErrorComponent | ApiV1S3ClustersListCreatedByComponentErrorComponent |
            ApiV1S3ClustersListCreatedByUsersErrorComponent | ApiV1S3ClustersListKindErrorComponent |
            ApiV1S3ClustersListNameErrorComponent | ApiV1S3ClustersListNameExactErrorComponent |
            ApiV1S3ClustersListOrganizationsErrorComponent | ApiV1S3ClustersListRegionErrorComponent |
            ApiV1S3ClustersListScopeErrorComponent | ApiV1S3ClustersListSearchErrorComponent |
            ApiV1S3ClustersListStateErrorComponent | ApiV1S3ClustersListStateNotErrorComponent |
            ApiV1S3ClustersListTimeRangeErrorComponent | ApiV1S3ClustersListUpdatedAtErrorComponent |
            ApiV1S3ClustersListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1S3ClustersListCreatedAtErrorComponent
        | ApiV1S3ClustersListCreatedByComponentErrorComponent
        | ApiV1S3ClustersListCreatedByUsersErrorComponent
        | ApiV1S3ClustersListKindErrorComponent
        | ApiV1S3ClustersListNameErrorComponent
        | ApiV1S3ClustersListNameExactErrorComponent
        | ApiV1S3ClustersListOrganizationsErrorComponent
        | ApiV1S3ClustersListRegionErrorComponent
        | ApiV1S3ClustersListScopeErrorComponent
        | ApiV1S3ClustersListSearchErrorComponent
        | ApiV1S3ClustersListStateErrorComponent
        | ApiV1S3ClustersListStateNotErrorComponent
        | ApiV1S3ClustersListTimeRangeErrorComponent
        | ApiV1S3ClustersListUpdatedAtErrorComponent
        | ApiV1S3ClustersListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1s3_clusters_list_created_at_error_component import (
            ApiV1S3ClustersListCreatedAtErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_created_by_component_error_component import (
            ApiV1S3ClustersListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_created_by_users_error_component import (
            ApiV1S3ClustersListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_kind_error_component import ApiV1S3ClustersListKindErrorComponent
        from ..models.api_v1s3_clusters_list_name_error_component import ApiV1S3ClustersListNameErrorComponent
        from ..models.api_v1s3_clusters_list_organizations_error_component import (
            ApiV1S3ClustersListOrganizationsErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_region_error_component import ApiV1S3ClustersListRegionErrorComponent
        from ..models.api_v1s3_clusters_list_scope_error_component import ApiV1S3ClustersListScopeErrorComponent
        from ..models.api_v1s3_clusters_list_search_error_component import ApiV1S3ClustersListSearchErrorComponent
        from ..models.api_v1s3_clusters_list_state_error_component import ApiV1S3ClustersListStateErrorComponent
        from ..models.api_v1s3_clusters_list_state_not_error_component import ApiV1S3ClustersListStateNotErrorComponent
        from ..models.api_v1s3_clusters_list_time_range_error_component import (
            ApiV1S3ClustersListTimeRangeErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_updated_at_error_component import (
            ApiV1S3ClustersListUpdatedAtErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_workspaces_error_component import (
            ApiV1S3ClustersListWorkspacesErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1S3ClustersListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersListStateNotErrorComponent):
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
        from ..models.api_v1s3_clusters_list_created_at_error_component import (
            ApiV1S3ClustersListCreatedAtErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_created_by_component_error_component import (
            ApiV1S3ClustersListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_created_by_users_error_component import (
            ApiV1S3ClustersListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_kind_error_component import ApiV1S3ClustersListKindErrorComponent
        from ..models.api_v1s3_clusters_list_name_error_component import ApiV1S3ClustersListNameErrorComponent
        from ..models.api_v1s3_clusters_list_name_exact_error_component import (
            ApiV1S3ClustersListNameExactErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_organizations_error_component import (
            ApiV1S3ClustersListOrganizationsErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_region_error_component import ApiV1S3ClustersListRegionErrorComponent
        from ..models.api_v1s3_clusters_list_scope_error_component import ApiV1S3ClustersListScopeErrorComponent
        from ..models.api_v1s3_clusters_list_search_error_component import ApiV1S3ClustersListSearchErrorComponent
        from ..models.api_v1s3_clusters_list_state_error_component import ApiV1S3ClustersListStateErrorComponent
        from ..models.api_v1s3_clusters_list_state_not_error_component import ApiV1S3ClustersListStateNotErrorComponent
        from ..models.api_v1s3_clusters_list_time_range_error_component import (
            ApiV1S3ClustersListTimeRangeErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_updated_at_error_component import (
            ApiV1S3ClustersListUpdatedAtErrorComponent,
        )
        from ..models.api_v1s3_clusters_list_workspaces_error_component import (
            ApiV1S3ClustersListWorkspacesErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1S3ClustersListCreatedAtErrorComponent
                | ApiV1S3ClustersListCreatedByComponentErrorComponent
                | ApiV1S3ClustersListCreatedByUsersErrorComponent
                | ApiV1S3ClustersListKindErrorComponent
                | ApiV1S3ClustersListNameErrorComponent
                | ApiV1S3ClustersListNameExactErrorComponent
                | ApiV1S3ClustersListOrganizationsErrorComponent
                | ApiV1S3ClustersListRegionErrorComponent
                | ApiV1S3ClustersListScopeErrorComponent
                | ApiV1S3ClustersListSearchErrorComponent
                | ApiV1S3ClustersListStateErrorComponent
                | ApiV1S3ClustersListStateNotErrorComponent
                | ApiV1S3ClustersListTimeRangeErrorComponent
                | ApiV1S3ClustersListUpdatedAtErrorComponent
                | ApiV1S3ClustersListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_0 = (
                        ApiV1S3ClustersListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_1 = (
                        ApiV1S3ClustersListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_2 = (
                        ApiV1S3ClustersListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_3 = (
                        ApiV1S3ClustersListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_4 = (
                        ApiV1S3ClustersListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_5 = (
                        ApiV1S3ClustersListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_6 = (
                        ApiV1S3ClustersListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_7 = (
                        ApiV1S3ClustersListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_8 = (
                        ApiV1S3ClustersListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_9 = (
                        ApiV1S3ClustersListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_10 = (
                        ApiV1S3ClustersListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_11 = (
                        ApiV1S3ClustersListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_12 = (
                        ApiV1S3ClustersListRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_list_error_type_13 = (
                        ApiV1S3ClustersListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1s3_clusters_list_error_type_14 = (
                    ApiV1S3ClustersListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1s3_clusters_list_error_type_14

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1s3_clusters_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1s3_clusters_list_validation_error.additional_properties = d
        return api_v1s3_clusters_list_validation_error

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
