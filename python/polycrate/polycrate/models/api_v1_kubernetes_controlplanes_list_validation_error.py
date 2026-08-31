from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_controlplanes_list_created_at_error_component import (
        ApiV1KubernetesControlplanesListCreatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_created_by_component_error_component import (
        ApiV1KubernetesControlplanesListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_created_by_users_error_component import (
        ApiV1KubernetesControlplanesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_kind_error_component import (
        ApiV1KubernetesControlplanesListKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_loadbalancer_mode_error_component import (
        ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_name_error_component import (
        ApiV1KubernetesControlplanesListNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_name_exact_error_component import (
        ApiV1KubernetesControlplanesListNameExactErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_organizations_error_component import (
        ApiV1KubernetesControlplanesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_region_error_component import (
        ApiV1KubernetesControlplanesListRegionErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_scope_error_component import (
        ApiV1KubernetesControlplanesListScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_search_error_component import (
        ApiV1KubernetesControlplanesListSearchErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_state_error_component import (
        ApiV1KubernetesControlplanesListStateErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_state_not_error_component import (
        ApiV1KubernetesControlplanesListStateNotErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_storage_class_error_component import (
        ApiV1KubernetesControlplanesListStorageClassErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_time_range_error_component import (
        ApiV1KubernetesControlplanesListTimeRangeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_updated_at_error_component import (
        ApiV1KubernetesControlplanesListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_list_workspaces_error_component import (
        ApiV1KubernetesControlplanesListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesControlplanesListValidationError")


@_attrs_define
class ApiV1KubernetesControlplanesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesControlplanesListCreatedAtErrorComponent |
            ApiV1KubernetesControlplanesListCreatedByComponentErrorComponent |
            ApiV1KubernetesControlplanesListCreatedByUsersErrorComponent |
            ApiV1KubernetesControlplanesListKindErrorComponent |
            ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponent |
            ApiV1KubernetesControlplanesListNameErrorComponent | ApiV1KubernetesControlplanesListNameExactErrorComponent |
            ApiV1KubernetesControlplanesListOrganizationsErrorComponent |
            ApiV1KubernetesControlplanesListRegionErrorComponent | ApiV1KubernetesControlplanesListScopeErrorComponent |
            ApiV1KubernetesControlplanesListSearchErrorComponent | ApiV1KubernetesControlplanesListStateErrorComponent |
            ApiV1KubernetesControlplanesListStateNotErrorComponent |
            ApiV1KubernetesControlplanesListStorageClassErrorComponent |
            ApiV1KubernetesControlplanesListTimeRangeErrorComponent |
            ApiV1KubernetesControlplanesListUpdatedAtErrorComponent |
            ApiV1KubernetesControlplanesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesControlplanesListCreatedAtErrorComponent
        | ApiV1KubernetesControlplanesListCreatedByComponentErrorComponent
        | ApiV1KubernetesControlplanesListCreatedByUsersErrorComponent
        | ApiV1KubernetesControlplanesListKindErrorComponent
        | ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponent
        | ApiV1KubernetesControlplanesListNameErrorComponent
        | ApiV1KubernetesControlplanesListNameExactErrorComponent
        | ApiV1KubernetesControlplanesListOrganizationsErrorComponent
        | ApiV1KubernetesControlplanesListRegionErrorComponent
        | ApiV1KubernetesControlplanesListScopeErrorComponent
        | ApiV1KubernetesControlplanesListSearchErrorComponent
        | ApiV1KubernetesControlplanesListStateErrorComponent
        | ApiV1KubernetesControlplanesListStateNotErrorComponent
        | ApiV1KubernetesControlplanesListStorageClassErrorComponent
        | ApiV1KubernetesControlplanesListTimeRangeErrorComponent
        | ApiV1KubernetesControlplanesListUpdatedAtErrorComponent
        | ApiV1KubernetesControlplanesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_controlplanes_list_created_at_error_component import (
            ApiV1KubernetesControlplanesListCreatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_created_by_component_error_component import (
            ApiV1KubernetesControlplanesListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_created_by_users_error_component import (
            ApiV1KubernetesControlplanesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_kind_error_component import (
            ApiV1KubernetesControlplanesListKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_name_error_component import (
            ApiV1KubernetesControlplanesListNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_organizations_error_component import (
            ApiV1KubernetesControlplanesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_region_error_component import (
            ApiV1KubernetesControlplanesListRegionErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_scope_error_component import (
            ApiV1KubernetesControlplanesListScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_search_error_component import (
            ApiV1KubernetesControlplanesListSearchErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_state_error_component import (
            ApiV1KubernetesControlplanesListStateErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_state_not_error_component import (
            ApiV1KubernetesControlplanesListStateNotErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_storage_class_error_component import (
            ApiV1KubernetesControlplanesListStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_time_range_error_component import (
            ApiV1KubernetesControlplanesListTimeRangeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_updated_at_error_component import (
            ApiV1KubernetesControlplanesListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_workspaces_error_component import (
            ApiV1KubernetesControlplanesListWorkspacesErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesControlplanesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesListStateNotErrorComponent):
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
        from ..models.api_v1_kubernetes_controlplanes_list_created_at_error_component import (
            ApiV1KubernetesControlplanesListCreatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_created_by_component_error_component import (
            ApiV1KubernetesControlplanesListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_created_by_users_error_component import (
            ApiV1KubernetesControlplanesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_kind_error_component import (
            ApiV1KubernetesControlplanesListKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_name_error_component import (
            ApiV1KubernetesControlplanesListNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_name_exact_error_component import (
            ApiV1KubernetesControlplanesListNameExactErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_organizations_error_component import (
            ApiV1KubernetesControlplanesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_region_error_component import (
            ApiV1KubernetesControlplanesListRegionErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_scope_error_component import (
            ApiV1KubernetesControlplanesListScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_search_error_component import (
            ApiV1KubernetesControlplanesListSearchErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_state_error_component import (
            ApiV1KubernetesControlplanesListStateErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_state_not_error_component import (
            ApiV1KubernetesControlplanesListStateNotErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_storage_class_error_component import (
            ApiV1KubernetesControlplanesListStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_time_range_error_component import (
            ApiV1KubernetesControlplanesListTimeRangeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_updated_at_error_component import (
            ApiV1KubernetesControlplanesListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_list_workspaces_error_component import (
            ApiV1KubernetesControlplanesListWorkspacesErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesControlplanesListCreatedAtErrorComponent
                | ApiV1KubernetesControlplanesListCreatedByComponentErrorComponent
                | ApiV1KubernetesControlplanesListCreatedByUsersErrorComponent
                | ApiV1KubernetesControlplanesListKindErrorComponent
                | ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponent
                | ApiV1KubernetesControlplanesListNameErrorComponent
                | ApiV1KubernetesControlplanesListNameExactErrorComponent
                | ApiV1KubernetesControlplanesListOrganizationsErrorComponent
                | ApiV1KubernetesControlplanesListRegionErrorComponent
                | ApiV1KubernetesControlplanesListScopeErrorComponent
                | ApiV1KubernetesControlplanesListSearchErrorComponent
                | ApiV1KubernetesControlplanesListStateErrorComponent
                | ApiV1KubernetesControlplanesListStateNotErrorComponent
                | ApiV1KubernetesControlplanesListStorageClassErrorComponent
                | ApiV1KubernetesControlplanesListTimeRangeErrorComponent
                | ApiV1KubernetesControlplanesListUpdatedAtErrorComponent
                | ApiV1KubernetesControlplanesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_0 = (
                        ApiV1KubernetesControlplanesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_1 = (
                        ApiV1KubernetesControlplanesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_2 = (
                        ApiV1KubernetesControlplanesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_3 = (
                        ApiV1KubernetesControlplanesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_4 = (
                        ApiV1KubernetesControlplanesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_5 = (
                        ApiV1KubernetesControlplanesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_6 = (
                        ApiV1KubernetesControlplanesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_7 = (
                        ApiV1KubernetesControlplanesListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_8 = (
                        ApiV1KubernetesControlplanesListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_9 = (
                        ApiV1KubernetesControlplanesListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_10 = (
                        ApiV1KubernetesControlplanesListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_11 = (
                        ApiV1KubernetesControlplanesListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_12 = (
                        ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_13 = (
                        ApiV1KubernetesControlplanesListStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_14 = (
                        ApiV1KubernetesControlplanesListRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_15 = (
                        ApiV1KubernetesControlplanesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_16 = (
                    ApiV1KubernetesControlplanesListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_controlplanes_list_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_controlplanes_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_controlplanes_list_validation_error.additional_properties = d
        return api_v1_kubernetes_controlplanes_list_validation_error

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
