from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_worker_pools_list_controlplane_error_component import (
        ApiV1KubernetesWorkerPoolsListControlplaneErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_created_at_error_component import (
        ApiV1KubernetesWorkerPoolsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_created_by_component_error_component import (
        ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_created_by_users_error_component import (
        ApiV1KubernetesWorkerPoolsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_desired_count_error_component import (
        ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_kind_error_component import (
        ApiV1KubernetesWorkerPoolsListKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_name_error_component import (
        ApiV1KubernetesWorkerPoolsListNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_name_exact_error_component import (
        ApiV1KubernetesWorkerPoolsListNameExactErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_organizations_error_component import (
        ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_provider_account_error_component import (
        ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_scope_error_component import (
        ApiV1KubernetesWorkerPoolsListScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_search_error_component import (
        ApiV1KubernetesWorkerPoolsListSearchErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_state_error_component import (
        ApiV1KubernetesWorkerPoolsListStateErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_state_not_error_component import (
        ApiV1KubernetesWorkerPoolsListStateNotErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_time_range_error_component import (
        ApiV1KubernetesWorkerPoolsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_updated_at_error_component import (
        ApiV1KubernetesWorkerPoolsListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_list_workspaces_error_component import (
        ApiV1KubernetesWorkerPoolsListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesWorkerPoolsListValidationError")


@_attrs_define
class ApiV1KubernetesWorkerPoolsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesWorkerPoolsListControlplaneErrorComponent |
            ApiV1KubernetesWorkerPoolsListCreatedAtErrorComponent |
            ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponent |
            ApiV1KubernetesWorkerPoolsListCreatedByUsersErrorComponent |
            ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponent | ApiV1KubernetesWorkerPoolsListKindErrorComponent |
            ApiV1KubernetesWorkerPoolsListNameErrorComponent | ApiV1KubernetesWorkerPoolsListNameExactErrorComponent |
            ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponent |
            ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponent | ApiV1KubernetesWorkerPoolsListScopeErrorComponent
            | ApiV1KubernetesWorkerPoolsListSearchErrorComponent | ApiV1KubernetesWorkerPoolsListStateErrorComponent |
            ApiV1KubernetesWorkerPoolsListStateNotErrorComponent | ApiV1KubernetesWorkerPoolsListTimeRangeErrorComponent |
            ApiV1KubernetesWorkerPoolsListUpdatedAtErrorComponent |
            ApiV1KubernetesWorkerPoolsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesWorkerPoolsListControlplaneErrorComponent
        | ApiV1KubernetesWorkerPoolsListCreatedAtErrorComponent
        | ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponent
        | ApiV1KubernetesWorkerPoolsListCreatedByUsersErrorComponent
        | ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponent
        | ApiV1KubernetesWorkerPoolsListKindErrorComponent
        | ApiV1KubernetesWorkerPoolsListNameErrorComponent
        | ApiV1KubernetesWorkerPoolsListNameExactErrorComponent
        | ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponent
        | ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponent
        | ApiV1KubernetesWorkerPoolsListScopeErrorComponent
        | ApiV1KubernetesWorkerPoolsListSearchErrorComponent
        | ApiV1KubernetesWorkerPoolsListStateErrorComponent
        | ApiV1KubernetesWorkerPoolsListStateNotErrorComponent
        | ApiV1KubernetesWorkerPoolsListTimeRangeErrorComponent
        | ApiV1KubernetesWorkerPoolsListUpdatedAtErrorComponent
        | ApiV1KubernetesWorkerPoolsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_worker_pools_list_controlplane_error_component import (
            ApiV1KubernetesWorkerPoolsListControlplaneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_created_at_error_component import (
            ApiV1KubernetesWorkerPoolsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_created_by_component_error_component import (
            ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_created_by_users_error_component import (
            ApiV1KubernetesWorkerPoolsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_desired_count_error_component import (
            ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_kind_error_component import (
            ApiV1KubernetesWorkerPoolsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_name_error_component import (
            ApiV1KubernetesWorkerPoolsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_organizations_error_component import (
            ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_provider_account_error_component import (
            ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_scope_error_component import (
            ApiV1KubernetesWorkerPoolsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_search_error_component import (
            ApiV1KubernetesWorkerPoolsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_state_error_component import (
            ApiV1KubernetesWorkerPoolsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_state_not_error_component import (
            ApiV1KubernetesWorkerPoolsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_time_range_error_component import (
            ApiV1KubernetesWorkerPoolsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_updated_at_error_component import (
            ApiV1KubernetesWorkerPoolsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_workspaces_error_component import (
            ApiV1KubernetesWorkerPoolsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListControlplaneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsListStateNotErrorComponent):
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
        from ..models.api_v1_kubernetes_worker_pools_list_controlplane_error_component import (
            ApiV1KubernetesWorkerPoolsListControlplaneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_created_at_error_component import (
            ApiV1KubernetesWorkerPoolsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_created_by_component_error_component import (
            ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_created_by_users_error_component import (
            ApiV1KubernetesWorkerPoolsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_desired_count_error_component import (
            ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_kind_error_component import (
            ApiV1KubernetesWorkerPoolsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_name_error_component import (
            ApiV1KubernetesWorkerPoolsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_name_exact_error_component import (
            ApiV1KubernetesWorkerPoolsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_organizations_error_component import (
            ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_provider_account_error_component import (
            ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_scope_error_component import (
            ApiV1KubernetesWorkerPoolsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_search_error_component import (
            ApiV1KubernetesWorkerPoolsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_state_error_component import (
            ApiV1KubernetesWorkerPoolsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_state_not_error_component import (
            ApiV1KubernetesWorkerPoolsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_time_range_error_component import (
            ApiV1KubernetesWorkerPoolsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_updated_at_error_component import (
            ApiV1KubernetesWorkerPoolsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_list_workspaces_error_component import (
            ApiV1KubernetesWorkerPoolsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesWorkerPoolsListControlplaneErrorComponent
                | ApiV1KubernetesWorkerPoolsListCreatedAtErrorComponent
                | ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponent
                | ApiV1KubernetesWorkerPoolsListCreatedByUsersErrorComponent
                | ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponent
                | ApiV1KubernetesWorkerPoolsListKindErrorComponent
                | ApiV1KubernetesWorkerPoolsListNameErrorComponent
                | ApiV1KubernetesWorkerPoolsListNameExactErrorComponent
                | ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponent
                | ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponent
                | ApiV1KubernetesWorkerPoolsListScopeErrorComponent
                | ApiV1KubernetesWorkerPoolsListSearchErrorComponent
                | ApiV1KubernetesWorkerPoolsListStateErrorComponent
                | ApiV1KubernetesWorkerPoolsListStateNotErrorComponent
                | ApiV1KubernetesWorkerPoolsListTimeRangeErrorComponent
                | ApiV1KubernetesWorkerPoolsListUpdatedAtErrorComponent
                | ApiV1KubernetesWorkerPoolsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_0 = (
                        ApiV1KubernetesWorkerPoolsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_1 = (
                        ApiV1KubernetesWorkerPoolsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_2 = (
                        ApiV1KubernetesWorkerPoolsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_3 = (
                        ApiV1KubernetesWorkerPoolsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_4 = (
                        ApiV1KubernetesWorkerPoolsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_5 = (
                        ApiV1KubernetesWorkerPoolsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_6 = (
                        ApiV1KubernetesWorkerPoolsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_7 = (
                        ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_8 = (
                        ApiV1KubernetesWorkerPoolsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_9 = (
                        ApiV1KubernetesWorkerPoolsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_10 = (
                        ApiV1KubernetesWorkerPoolsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_11 = (
                        ApiV1KubernetesWorkerPoolsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_12 = (
                        ApiV1KubernetesWorkerPoolsListControlplaneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_13 = (
                        ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_14 = (
                        ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_15 = (
                        ApiV1KubernetesWorkerPoolsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_16 = (
                    ApiV1KubernetesWorkerPoolsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_worker_pools_list_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_worker_pools_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_worker_pools_list_validation_error.additional_properties = d
        return api_v1_kubernetes_worker_pools_list_validation_error

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
