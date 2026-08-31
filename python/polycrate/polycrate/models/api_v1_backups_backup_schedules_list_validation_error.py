from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_backups_backup_schedules_list_created_at_error_component import (
        ApiV1BackupsBackupSchedulesListCreatedAtErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_created_by_component_error_component import (
        ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_created_by_users_error_component import (
        ApiV1BackupsBackupSchedulesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_k8s_cluster_error_component import (
        ApiV1BackupsBackupSchedulesListK8SClusterErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_kind_error_component import (
        ApiV1BackupsBackupSchedulesListKindErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_name_error_component import (
        ApiV1BackupsBackupSchedulesListNameErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_name_exact_error_component import (
        ApiV1BackupsBackupSchedulesListNameExactErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_organizations_error_component import (
        ApiV1BackupsBackupSchedulesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_provider_error_component import (
        ApiV1BackupsBackupSchedulesListProviderErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_scope_error_component import (
        ApiV1BackupsBackupSchedulesListScopeErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_search_error_component import (
        ApiV1BackupsBackupSchedulesListSearchErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_source_namespace_error_component import (
        ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_state_error_component import (
        ApiV1BackupsBackupSchedulesListStateErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_state_not_error_component import (
        ApiV1BackupsBackupSchedulesListStateNotErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_status_error_component import (
        ApiV1BackupsBackupSchedulesListStatusErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_time_range_error_component import (
        ApiV1BackupsBackupSchedulesListTimeRangeErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_updated_at_error_component import (
        ApiV1BackupsBackupSchedulesListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_list_workspaces_error_component import (
        ApiV1BackupsBackupSchedulesListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BackupsBackupSchedulesListValidationError")


@_attrs_define
class ApiV1BackupsBackupSchedulesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BackupsBackupSchedulesListCreatedAtErrorComponent |
            ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponent |
            ApiV1BackupsBackupSchedulesListCreatedByUsersErrorComponent |
            ApiV1BackupsBackupSchedulesListK8SClusterErrorComponent | ApiV1BackupsBackupSchedulesListKindErrorComponent |
            ApiV1BackupsBackupSchedulesListNameErrorComponent | ApiV1BackupsBackupSchedulesListNameExactErrorComponent |
            ApiV1BackupsBackupSchedulesListOrganizationsErrorComponent |
            ApiV1BackupsBackupSchedulesListProviderErrorComponent | ApiV1BackupsBackupSchedulesListScopeErrorComponent |
            ApiV1BackupsBackupSchedulesListSearchErrorComponent |
            ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponent |
            ApiV1BackupsBackupSchedulesListStateErrorComponent | ApiV1BackupsBackupSchedulesListStateNotErrorComponent |
            ApiV1BackupsBackupSchedulesListStatusErrorComponent | ApiV1BackupsBackupSchedulesListTimeRangeErrorComponent |
            ApiV1BackupsBackupSchedulesListUpdatedAtErrorComponent |
            ApiV1BackupsBackupSchedulesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BackupsBackupSchedulesListCreatedAtErrorComponent
        | ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponent
        | ApiV1BackupsBackupSchedulesListCreatedByUsersErrorComponent
        | ApiV1BackupsBackupSchedulesListK8SClusterErrorComponent
        | ApiV1BackupsBackupSchedulesListKindErrorComponent
        | ApiV1BackupsBackupSchedulesListNameErrorComponent
        | ApiV1BackupsBackupSchedulesListNameExactErrorComponent
        | ApiV1BackupsBackupSchedulesListOrganizationsErrorComponent
        | ApiV1BackupsBackupSchedulesListProviderErrorComponent
        | ApiV1BackupsBackupSchedulesListScopeErrorComponent
        | ApiV1BackupsBackupSchedulesListSearchErrorComponent
        | ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponent
        | ApiV1BackupsBackupSchedulesListStateErrorComponent
        | ApiV1BackupsBackupSchedulesListStateNotErrorComponent
        | ApiV1BackupsBackupSchedulesListStatusErrorComponent
        | ApiV1BackupsBackupSchedulesListTimeRangeErrorComponent
        | ApiV1BackupsBackupSchedulesListUpdatedAtErrorComponent
        | ApiV1BackupsBackupSchedulesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_backups_backup_schedules_list_created_at_error_component import (
            ApiV1BackupsBackupSchedulesListCreatedAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_created_by_component_error_component import (
            ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_created_by_users_error_component import (
            ApiV1BackupsBackupSchedulesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_kind_error_component import (
            ApiV1BackupsBackupSchedulesListKindErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_name_error_component import (
            ApiV1BackupsBackupSchedulesListNameErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_name_exact_error_component import (
            ApiV1BackupsBackupSchedulesListNameExactErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_organizations_error_component import (
            ApiV1BackupsBackupSchedulesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_provider_error_component import (
            ApiV1BackupsBackupSchedulesListProviderErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_scope_error_component import (
            ApiV1BackupsBackupSchedulesListScopeErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_search_error_component import (
            ApiV1BackupsBackupSchedulesListSearchErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_source_namespace_error_component import (
            ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_state_error_component import (
            ApiV1BackupsBackupSchedulesListStateErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_state_not_error_component import (
            ApiV1BackupsBackupSchedulesListStateNotErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_status_error_component import (
            ApiV1BackupsBackupSchedulesListStatusErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_time_range_error_component import (
            ApiV1BackupsBackupSchedulesListTimeRangeErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_updated_at_error_component import (
            ApiV1BackupsBackupSchedulesListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_workspaces_error_component import (
            ApiV1BackupsBackupSchedulesListWorkspacesErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListNameExactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesListStatusErrorComponent):
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
        from ..models.api_v1_backups_backup_schedules_list_created_at_error_component import (
            ApiV1BackupsBackupSchedulesListCreatedAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_created_by_component_error_component import (
            ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_created_by_users_error_component import (
            ApiV1BackupsBackupSchedulesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_k8s_cluster_error_component import (
            ApiV1BackupsBackupSchedulesListK8SClusterErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_kind_error_component import (
            ApiV1BackupsBackupSchedulesListKindErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_name_error_component import (
            ApiV1BackupsBackupSchedulesListNameErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_name_exact_error_component import (
            ApiV1BackupsBackupSchedulesListNameExactErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_organizations_error_component import (
            ApiV1BackupsBackupSchedulesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_provider_error_component import (
            ApiV1BackupsBackupSchedulesListProviderErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_scope_error_component import (
            ApiV1BackupsBackupSchedulesListScopeErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_search_error_component import (
            ApiV1BackupsBackupSchedulesListSearchErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_source_namespace_error_component import (
            ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_state_error_component import (
            ApiV1BackupsBackupSchedulesListStateErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_state_not_error_component import (
            ApiV1BackupsBackupSchedulesListStateNotErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_status_error_component import (
            ApiV1BackupsBackupSchedulesListStatusErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_time_range_error_component import (
            ApiV1BackupsBackupSchedulesListTimeRangeErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_updated_at_error_component import (
            ApiV1BackupsBackupSchedulesListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_list_workspaces_error_component import (
            ApiV1BackupsBackupSchedulesListWorkspacesErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BackupsBackupSchedulesListCreatedAtErrorComponent
                | ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponent
                | ApiV1BackupsBackupSchedulesListCreatedByUsersErrorComponent
                | ApiV1BackupsBackupSchedulesListK8SClusterErrorComponent
                | ApiV1BackupsBackupSchedulesListKindErrorComponent
                | ApiV1BackupsBackupSchedulesListNameErrorComponent
                | ApiV1BackupsBackupSchedulesListNameExactErrorComponent
                | ApiV1BackupsBackupSchedulesListOrganizationsErrorComponent
                | ApiV1BackupsBackupSchedulesListProviderErrorComponent
                | ApiV1BackupsBackupSchedulesListScopeErrorComponent
                | ApiV1BackupsBackupSchedulesListSearchErrorComponent
                | ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponent
                | ApiV1BackupsBackupSchedulesListStateErrorComponent
                | ApiV1BackupsBackupSchedulesListStateNotErrorComponent
                | ApiV1BackupsBackupSchedulesListStatusErrorComponent
                | ApiV1BackupsBackupSchedulesListTimeRangeErrorComponent
                | ApiV1BackupsBackupSchedulesListUpdatedAtErrorComponent
                | ApiV1BackupsBackupSchedulesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_0 = (
                        ApiV1BackupsBackupSchedulesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_1 = (
                        ApiV1BackupsBackupSchedulesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_2 = (
                        ApiV1BackupsBackupSchedulesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_3 = (
                        ApiV1BackupsBackupSchedulesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_4 = (
                        ApiV1BackupsBackupSchedulesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_5 = (
                        ApiV1BackupsBackupSchedulesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_6 = (
                        ApiV1BackupsBackupSchedulesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_7 = (
                        ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_8 = (
                        ApiV1BackupsBackupSchedulesListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_9 = (
                        ApiV1BackupsBackupSchedulesListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_10 = (
                        ApiV1BackupsBackupSchedulesListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_11 = (
                        ApiV1BackupsBackupSchedulesListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_12 = (
                        ApiV1BackupsBackupSchedulesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_13 = (
                        ApiV1BackupsBackupSchedulesListNameExactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_14 = (
                        ApiV1BackupsBackupSchedulesListProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_15 = (
                        ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_list_error_type_16 = (
                        ApiV1BackupsBackupSchedulesListStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_list_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backup_schedules_list_error_type_17 = (
                    ApiV1BackupsBackupSchedulesListK8SClusterErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backup_schedules_list_error_type_17

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_backups_backup_schedules_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_backups_backup_schedules_list_validation_error.additional_properties = d
        return api_v1_backups_backup_schedules_list_validation_error

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
