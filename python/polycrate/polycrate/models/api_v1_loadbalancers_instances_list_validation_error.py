from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_loadbalancers_instances_list_created_at_error_component import (
        ApiV1LoadbalancersInstancesListCreatedAtErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_created_by_component_error_component import (
        ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_created_by_users_error_component import (
        ApiV1LoadbalancersInstancesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_kind_error_component import (
        ApiV1LoadbalancersInstancesListKindErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_loadbalancer_region_error_component import (
        ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_name_error_component import (
        ApiV1LoadbalancersInstancesListNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_name_exact_error_component import (
        ApiV1LoadbalancersInstancesListNameExactErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_organizations_error_component import (
        ApiV1LoadbalancersInstancesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_prefix_error_component import (
        ApiV1LoadbalancersInstancesListPrefixErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_region_error_component import (
        ApiV1LoadbalancersInstancesListRegionErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_scope_error_component import (
        ApiV1LoadbalancersInstancesListScopeErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_search_error_component import (
        ApiV1LoadbalancersInstancesListSearchErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_session_affinity_error_component import (
        ApiV1LoadbalancersInstancesListSessionAffinityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_state_error_component import (
        ApiV1LoadbalancersInstancesListStateErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_state_not_error_component import (
        ApiV1LoadbalancersInstancesListStateNotErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_time_range_error_component import (
        ApiV1LoadbalancersInstancesListTimeRangeErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_updated_at_error_component import (
        ApiV1LoadbalancersInstancesListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_list_workspaces_error_component import (
        ApiV1LoadbalancersInstancesListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1LoadbalancersInstancesListValidationError")


@_attrs_define
class ApiV1LoadbalancersInstancesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1LoadbalancersInstancesListCreatedAtErrorComponent |
            ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponent |
            ApiV1LoadbalancersInstancesListCreatedByUsersErrorComponent | ApiV1LoadbalancersInstancesListKindErrorComponent
            | ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponent |
            ApiV1LoadbalancersInstancesListNameErrorComponent | ApiV1LoadbalancersInstancesListNameExactErrorComponent |
            ApiV1LoadbalancersInstancesListOrganizationsErrorComponent | ApiV1LoadbalancersInstancesListPrefixErrorComponent
            | ApiV1LoadbalancersInstancesListRegionErrorComponent | ApiV1LoadbalancersInstancesListScopeErrorComponent |
            ApiV1LoadbalancersInstancesListSearchErrorComponent |
            ApiV1LoadbalancersInstancesListSessionAffinityErrorComponent |
            ApiV1LoadbalancersInstancesListStateErrorComponent | ApiV1LoadbalancersInstancesListStateNotErrorComponent |
            ApiV1LoadbalancersInstancesListTimeRangeErrorComponent | ApiV1LoadbalancersInstancesListUpdatedAtErrorComponent
            | ApiV1LoadbalancersInstancesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1LoadbalancersInstancesListCreatedAtErrorComponent
        | ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponent
        | ApiV1LoadbalancersInstancesListCreatedByUsersErrorComponent
        | ApiV1LoadbalancersInstancesListKindErrorComponent
        | ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponent
        | ApiV1LoadbalancersInstancesListNameErrorComponent
        | ApiV1LoadbalancersInstancesListNameExactErrorComponent
        | ApiV1LoadbalancersInstancesListOrganizationsErrorComponent
        | ApiV1LoadbalancersInstancesListPrefixErrorComponent
        | ApiV1LoadbalancersInstancesListRegionErrorComponent
        | ApiV1LoadbalancersInstancesListScopeErrorComponent
        | ApiV1LoadbalancersInstancesListSearchErrorComponent
        | ApiV1LoadbalancersInstancesListSessionAffinityErrorComponent
        | ApiV1LoadbalancersInstancesListStateErrorComponent
        | ApiV1LoadbalancersInstancesListStateNotErrorComponent
        | ApiV1LoadbalancersInstancesListTimeRangeErrorComponent
        | ApiV1LoadbalancersInstancesListUpdatedAtErrorComponent
        | ApiV1LoadbalancersInstancesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_loadbalancers_instances_list_created_at_error_component import (
            ApiV1LoadbalancersInstancesListCreatedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_created_by_component_error_component import (
            ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_created_by_users_error_component import (
            ApiV1LoadbalancersInstancesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_kind_error_component import (
            ApiV1LoadbalancersInstancesListKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_loadbalancer_region_error_component import (
            ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_name_error_component import (
            ApiV1LoadbalancersInstancesListNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_organizations_error_component import (
            ApiV1LoadbalancersInstancesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_prefix_error_component import (
            ApiV1LoadbalancersInstancesListPrefixErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_region_error_component import (
            ApiV1LoadbalancersInstancesListRegionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_scope_error_component import (
            ApiV1LoadbalancersInstancesListScopeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_search_error_component import (
            ApiV1LoadbalancersInstancesListSearchErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_session_affinity_error_component import (
            ApiV1LoadbalancersInstancesListSessionAffinityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_state_error_component import (
            ApiV1LoadbalancersInstancesListStateErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_state_not_error_component import (
            ApiV1LoadbalancersInstancesListStateNotErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_time_range_error_component import (
            ApiV1LoadbalancersInstancesListTimeRangeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_updated_at_error_component import (
            ApiV1LoadbalancersInstancesListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_workspaces_error_component import (
            ApiV1LoadbalancersInstancesListWorkspacesErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1LoadbalancersInstancesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListSessionAffinityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListPrefixErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesListStateNotErrorComponent):
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
        from ..models.api_v1_loadbalancers_instances_list_created_at_error_component import (
            ApiV1LoadbalancersInstancesListCreatedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_created_by_component_error_component import (
            ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_created_by_users_error_component import (
            ApiV1LoadbalancersInstancesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_kind_error_component import (
            ApiV1LoadbalancersInstancesListKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_loadbalancer_region_error_component import (
            ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_name_error_component import (
            ApiV1LoadbalancersInstancesListNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_name_exact_error_component import (
            ApiV1LoadbalancersInstancesListNameExactErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_organizations_error_component import (
            ApiV1LoadbalancersInstancesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_prefix_error_component import (
            ApiV1LoadbalancersInstancesListPrefixErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_region_error_component import (
            ApiV1LoadbalancersInstancesListRegionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_scope_error_component import (
            ApiV1LoadbalancersInstancesListScopeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_search_error_component import (
            ApiV1LoadbalancersInstancesListSearchErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_session_affinity_error_component import (
            ApiV1LoadbalancersInstancesListSessionAffinityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_state_error_component import (
            ApiV1LoadbalancersInstancesListStateErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_state_not_error_component import (
            ApiV1LoadbalancersInstancesListStateNotErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_time_range_error_component import (
            ApiV1LoadbalancersInstancesListTimeRangeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_updated_at_error_component import (
            ApiV1LoadbalancersInstancesListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_instances_list_workspaces_error_component import (
            ApiV1LoadbalancersInstancesListWorkspacesErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1LoadbalancersInstancesListCreatedAtErrorComponent
                | ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponent
                | ApiV1LoadbalancersInstancesListCreatedByUsersErrorComponent
                | ApiV1LoadbalancersInstancesListKindErrorComponent
                | ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponent
                | ApiV1LoadbalancersInstancesListNameErrorComponent
                | ApiV1LoadbalancersInstancesListNameExactErrorComponent
                | ApiV1LoadbalancersInstancesListOrganizationsErrorComponent
                | ApiV1LoadbalancersInstancesListPrefixErrorComponent
                | ApiV1LoadbalancersInstancesListRegionErrorComponent
                | ApiV1LoadbalancersInstancesListScopeErrorComponent
                | ApiV1LoadbalancersInstancesListSearchErrorComponent
                | ApiV1LoadbalancersInstancesListSessionAffinityErrorComponent
                | ApiV1LoadbalancersInstancesListStateErrorComponent
                | ApiV1LoadbalancersInstancesListStateNotErrorComponent
                | ApiV1LoadbalancersInstancesListTimeRangeErrorComponent
                | ApiV1LoadbalancersInstancesListUpdatedAtErrorComponent
                | ApiV1LoadbalancersInstancesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_0 = (
                        ApiV1LoadbalancersInstancesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_1 = (
                        ApiV1LoadbalancersInstancesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_2 = (
                        ApiV1LoadbalancersInstancesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_3 = (
                        ApiV1LoadbalancersInstancesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_4 = (
                        ApiV1LoadbalancersInstancesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_5 = (
                        ApiV1LoadbalancersInstancesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_6 = (
                        ApiV1LoadbalancersInstancesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_7 = (
                        ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_8 = (
                        ApiV1LoadbalancersInstancesListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_9 = (
                        ApiV1LoadbalancersInstancesListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_10 = (
                        ApiV1LoadbalancersInstancesListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_11 = (
                        ApiV1LoadbalancersInstancesListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_12 = (
                        ApiV1LoadbalancersInstancesListSessionAffinityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_13 = (
                        ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_14 = (
                        ApiV1LoadbalancersInstancesListRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_15 = (
                        ApiV1LoadbalancersInstancesListPrefixErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_list_error_type_16 = (
                        ApiV1LoadbalancersInstancesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_list_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_loadbalancers_instances_list_error_type_17 = (
                    ApiV1LoadbalancersInstancesListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_loadbalancers_instances_list_error_type_17

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_loadbalancers_instances_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_loadbalancers_instances_list_validation_error.additional_properties = d
        return api_v1_loadbalancers_instances_list_validation_error

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
