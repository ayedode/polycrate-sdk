from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_hosts_list_bootstrap_status_error_component import ApiV1HostsListBootstrapStatusErrorComponent
    from ..models.api_v1_hosts_list_created_at_error_component import ApiV1HostsListCreatedAtErrorComponent
    from ..models.api_v1_hosts_list_created_by_component_error_component import (
        ApiV1HostsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_hosts_list_created_by_users_error_component import ApiV1HostsListCreatedByUsersErrorComponent
    from ..models.api_v1_hosts_list_hostname_error_component import ApiV1HostsListHostnameErrorComponent
    from ..models.api_v1_hosts_list_incidents_error_component import ApiV1HostsListIncidentsErrorComponent
    from ..models.api_v1_hosts_list_kind_error_component import ApiV1HostsListKindErrorComponent
    from ..models.api_v1_hosts_list_maintenances_error_component import ApiV1HostsListMaintenancesErrorComponent
    from ..models.api_v1_hosts_list_name_error_component import ApiV1HostsListNameErrorComponent
    from ..models.api_v1_hosts_list_name_exact_error_component import ApiV1HostsListNameExactErrorComponent
    from ..models.api_v1_hosts_list_organizations_error_component import ApiV1HostsListOrganizationsErrorComponent
    from ..models.api_v1_hosts_list_provider_account_error_component import ApiV1HostsListProviderAccountErrorComponent
    from ..models.api_v1_hosts_list_provider_datacenter_error_component import (
        ApiV1HostsListProviderDatacenterErrorComponent,
    )
    from ..models.api_v1_hosts_list_provider_error_component import ApiV1HostsListProviderErrorComponent
    from ..models.api_v1_hosts_list_provider_image_os_architecture_error_component import (
        ApiV1HostsListProviderImageOsArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_list_provider_image_os_flavor_error_component import (
        ApiV1HostsListProviderImageOsFlavorErrorComponent,
    )
    from ..models.api_v1_hosts_list_provider_image_os_version_error_component import (
        ApiV1HostsListProviderImageOsVersionErrorComponent,
    )
    from ..models.api_v1_hosts_list_provider_type_error_component import ApiV1HostsListProviderTypeErrorComponent
    from ..models.api_v1_hosts_list_resource_cpu_architecture_error_component import (
        ApiV1HostsListResourceCpuArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_list_resource_cpu_cores_error_component import (
        ApiV1HostsListResourceCpuCoresErrorComponent,
    )
    from ..models.api_v1_hosts_list_resource_cpu_type_error_component import ApiV1HostsListResourceCpuTypeErrorComponent
    from ..models.api_v1_hosts_list_resource_disk_error_component import ApiV1HostsListResourceDiskErrorComponent
    from ..models.api_v1_hosts_list_resource_memory_error_component import ApiV1HostsListResourceMemoryErrorComponent
    from ..models.api_v1_hosts_list_role_error_component import ApiV1HostsListRoleErrorComponent
    from ..models.api_v1_hosts_list_scope_error_component import ApiV1HostsListScopeErrorComponent
    from ..models.api_v1_hosts_list_search_error_component import ApiV1HostsListSearchErrorComponent
    from ..models.api_v1_hosts_list_state_error_component import ApiV1HostsListStateErrorComponent
    from ..models.api_v1_hosts_list_state_not_error_component import ApiV1HostsListStateNotErrorComponent
    from ..models.api_v1_hosts_list_time_range_error_component import ApiV1HostsListTimeRangeErrorComponent
    from ..models.api_v1_hosts_list_updated_at_error_component import ApiV1HostsListUpdatedAtErrorComponent
    from ..models.api_v1_hosts_list_workspaces_error_component import ApiV1HostsListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1HostsListValidationError")


@_attrs_define
class ApiV1HostsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1HostsListBootstrapStatusErrorComponent | ApiV1HostsListCreatedAtErrorComponent |
            ApiV1HostsListCreatedByComponentErrorComponent | ApiV1HostsListCreatedByUsersErrorComponent |
            ApiV1HostsListHostnameErrorComponent | ApiV1HostsListIncidentsErrorComponent | ApiV1HostsListKindErrorComponent
            | ApiV1HostsListMaintenancesErrorComponent | ApiV1HostsListNameErrorComponent |
            ApiV1HostsListNameExactErrorComponent | ApiV1HostsListOrganizationsErrorComponent |
            ApiV1HostsListProviderAccountErrorComponent | ApiV1HostsListProviderDatacenterErrorComponent |
            ApiV1HostsListProviderErrorComponent | ApiV1HostsListProviderImageOsArchitectureErrorComponent |
            ApiV1HostsListProviderImageOsFlavorErrorComponent | ApiV1HostsListProviderImageOsVersionErrorComponent |
            ApiV1HostsListProviderTypeErrorComponent | ApiV1HostsListResourceCpuArchitectureErrorComponent |
            ApiV1HostsListResourceCpuCoresErrorComponent | ApiV1HostsListResourceCpuTypeErrorComponent |
            ApiV1HostsListResourceDiskErrorComponent | ApiV1HostsListResourceMemoryErrorComponent |
            ApiV1HostsListRoleErrorComponent | ApiV1HostsListScopeErrorComponent | ApiV1HostsListSearchErrorComponent |
            ApiV1HostsListStateErrorComponent | ApiV1HostsListStateNotErrorComponent | ApiV1HostsListTimeRangeErrorComponent
            | ApiV1HostsListUpdatedAtErrorComponent | ApiV1HostsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1HostsListBootstrapStatusErrorComponent
        | ApiV1HostsListCreatedAtErrorComponent
        | ApiV1HostsListCreatedByComponentErrorComponent
        | ApiV1HostsListCreatedByUsersErrorComponent
        | ApiV1HostsListHostnameErrorComponent
        | ApiV1HostsListIncidentsErrorComponent
        | ApiV1HostsListKindErrorComponent
        | ApiV1HostsListMaintenancesErrorComponent
        | ApiV1HostsListNameErrorComponent
        | ApiV1HostsListNameExactErrorComponent
        | ApiV1HostsListOrganizationsErrorComponent
        | ApiV1HostsListProviderAccountErrorComponent
        | ApiV1HostsListProviderDatacenterErrorComponent
        | ApiV1HostsListProviderErrorComponent
        | ApiV1HostsListProviderImageOsArchitectureErrorComponent
        | ApiV1HostsListProviderImageOsFlavorErrorComponent
        | ApiV1HostsListProviderImageOsVersionErrorComponent
        | ApiV1HostsListProviderTypeErrorComponent
        | ApiV1HostsListResourceCpuArchitectureErrorComponent
        | ApiV1HostsListResourceCpuCoresErrorComponent
        | ApiV1HostsListResourceCpuTypeErrorComponent
        | ApiV1HostsListResourceDiskErrorComponent
        | ApiV1HostsListResourceMemoryErrorComponent
        | ApiV1HostsListRoleErrorComponent
        | ApiV1HostsListScopeErrorComponent
        | ApiV1HostsListSearchErrorComponent
        | ApiV1HostsListStateErrorComponent
        | ApiV1HostsListStateNotErrorComponent
        | ApiV1HostsListTimeRangeErrorComponent
        | ApiV1HostsListUpdatedAtErrorComponent
        | ApiV1HostsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_hosts_list_bootstrap_status_error_component import (
            ApiV1HostsListBootstrapStatusErrorComponent,
        )
        from ..models.api_v1_hosts_list_created_at_error_component import ApiV1HostsListCreatedAtErrorComponent
        from ..models.api_v1_hosts_list_created_by_component_error_component import (
            ApiV1HostsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_list_created_by_users_error_component import (
            ApiV1HostsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_hosts_list_hostname_error_component import ApiV1HostsListHostnameErrorComponent
        from ..models.api_v1_hosts_list_incidents_error_component import ApiV1HostsListIncidentsErrorComponent
        from ..models.api_v1_hosts_list_kind_error_component import ApiV1HostsListKindErrorComponent
        from ..models.api_v1_hosts_list_maintenances_error_component import ApiV1HostsListMaintenancesErrorComponent
        from ..models.api_v1_hosts_list_name_error_component import ApiV1HostsListNameErrorComponent
        from ..models.api_v1_hosts_list_organizations_error_component import ApiV1HostsListOrganizationsErrorComponent
        from ..models.api_v1_hosts_list_provider_account_error_component import (
            ApiV1HostsListProviderAccountErrorComponent,
        )
        from ..models.api_v1_hosts_list_provider_datacenter_error_component import (
            ApiV1HostsListProviderDatacenterErrorComponent,
        )
        from ..models.api_v1_hosts_list_provider_error_component import ApiV1HostsListProviderErrorComponent
        from ..models.api_v1_hosts_list_provider_image_os_architecture_error_component import (
            ApiV1HostsListProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_list_provider_image_os_flavor_error_component import (
            ApiV1HostsListProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_list_provider_image_os_version_error_component import (
            ApiV1HostsListProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_list_provider_type_error_component import ApiV1HostsListProviderTypeErrorComponent
        from ..models.api_v1_hosts_list_resource_cpu_architecture_error_component import (
            ApiV1HostsListResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_list_resource_cpu_cores_error_component import (
            ApiV1HostsListResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_list_resource_cpu_type_error_component import (
            ApiV1HostsListResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_list_resource_disk_error_component import ApiV1HostsListResourceDiskErrorComponent
        from ..models.api_v1_hosts_list_resource_memory_error_component import (
            ApiV1HostsListResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_list_role_error_component import ApiV1HostsListRoleErrorComponent
        from ..models.api_v1_hosts_list_scope_error_component import ApiV1HostsListScopeErrorComponent
        from ..models.api_v1_hosts_list_search_error_component import ApiV1HostsListSearchErrorComponent
        from ..models.api_v1_hosts_list_state_error_component import ApiV1HostsListStateErrorComponent
        from ..models.api_v1_hosts_list_state_not_error_component import ApiV1HostsListStateNotErrorComponent
        from ..models.api_v1_hosts_list_time_range_error_component import ApiV1HostsListTimeRangeErrorComponent
        from ..models.api_v1_hosts_list_updated_at_error_component import ApiV1HostsListUpdatedAtErrorComponent
        from ..models.api_v1_hosts_list_workspaces_error_component import ApiV1HostsListWorkspacesErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1HostsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListResourceCpuCoresErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListResourceCpuTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListResourceCpuArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListResourceMemoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListResourceDiskErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListProviderTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListProviderImageOsFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListProviderImageOsVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListProviderImageOsArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListProviderDatacenterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListMaintenancesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListIncidentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListBootstrapStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListProviderAccountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsListStateNotErrorComponent):
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
        from ..models.api_v1_hosts_list_bootstrap_status_error_component import (
            ApiV1HostsListBootstrapStatusErrorComponent,
        )
        from ..models.api_v1_hosts_list_created_at_error_component import ApiV1HostsListCreatedAtErrorComponent
        from ..models.api_v1_hosts_list_created_by_component_error_component import (
            ApiV1HostsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_list_created_by_users_error_component import (
            ApiV1HostsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_hosts_list_hostname_error_component import ApiV1HostsListHostnameErrorComponent
        from ..models.api_v1_hosts_list_incidents_error_component import ApiV1HostsListIncidentsErrorComponent
        from ..models.api_v1_hosts_list_kind_error_component import ApiV1HostsListKindErrorComponent
        from ..models.api_v1_hosts_list_maintenances_error_component import ApiV1HostsListMaintenancesErrorComponent
        from ..models.api_v1_hosts_list_name_error_component import ApiV1HostsListNameErrorComponent
        from ..models.api_v1_hosts_list_name_exact_error_component import ApiV1HostsListNameExactErrorComponent
        from ..models.api_v1_hosts_list_organizations_error_component import ApiV1HostsListOrganizationsErrorComponent
        from ..models.api_v1_hosts_list_provider_account_error_component import (
            ApiV1HostsListProviderAccountErrorComponent,
        )
        from ..models.api_v1_hosts_list_provider_datacenter_error_component import (
            ApiV1HostsListProviderDatacenterErrorComponent,
        )
        from ..models.api_v1_hosts_list_provider_error_component import ApiV1HostsListProviderErrorComponent
        from ..models.api_v1_hosts_list_provider_image_os_architecture_error_component import (
            ApiV1HostsListProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_list_provider_image_os_flavor_error_component import (
            ApiV1HostsListProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_list_provider_image_os_version_error_component import (
            ApiV1HostsListProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_list_provider_type_error_component import ApiV1HostsListProviderTypeErrorComponent
        from ..models.api_v1_hosts_list_resource_cpu_architecture_error_component import (
            ApiV1HostsListResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_list_resource_cpu_cores_error_component import (
            ApiV1HostsListResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_list_resource_cpu_type_error_component import (
            ApiV1HostsListResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_list_resource_disk_error_component import ApiV1HostsListResourceDiskErrorComponent
        from ..models.api_v1_hosts_list_resource_memory_error_component import (
            ApiV1HostsListResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_list_role_error_component import ApiV1HostsListRoleErrorComponent
        from ..models.api_v1_hosts_list_scope_error_component import ApiV1HostsListScopeErrorComponent
        from ..models.api_v1_hosts_list_search_error_component import ApiV1HostsListSearchErrorComponent
        from ..models.api_v1_hosts_list_state_error_component import ApiV1HostsListStateErrorComponent
        from ..models.api_v1_hosts_list_state_not_error_component import ApiV1HostsListStateNotErrorComponent
        from ..models.api_v1_hosts_list_time_range_error_component import ApiV1HostsListTimeRangeErrorComponent
        from ..models.api_v1_hosts_list_updated_at_error_component import ApiV1HostsListUpdatedAtErrorComponent
        from ..models.api_v1_hosts_list_workspaces_error_component import ApiV1HostsListWorkspacesErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1HostsListBootstrapStatusErrorComponent
                | ApiV1HostsListCreatedAtErrorComponent
                | ApiV1HostsListCreatedByComponentErrorComponent
                | ApiV1HostsListCreatedByUsersErrorComponent
                | ApiV1HostsListHostnameErrorComponent
                | ApiV1HostsListIncidentsErrorComponent
                | ApiV1HostsListKindErrorComponent
                | ApiV1HostsListMaintenancesErrorComponent
                | ApiV1HostsListNameErrorComponent
                | ApiV1HostsListNameExactErrorComponent
                | ApiV1HostsListOrganizationsErrorComponent
                | ApiV1HostsListProviderAccountErrorComponent
                | ApiV1HostsListProviderDatacenterErrorComponent
                | ApiV1HostsListProviderErrorComponent
                | ApiV1HostsListProviderImageOsArchitectureErrorComponent
                | ApiV1HostsListProviderImageOsFlavorErrorComponent
                | ApiV1HostsListProviderImageOsVersionErrorComponent
                | ApiV1HostsListProviderTypeErrorComponent
                | ApiV1HostsListResourceCpuArchitectureErrorComponent
                | ApiV1HostsListResourceCpuCoresErrorComponent
                | ApiV1HostsListResourceCpuTypeErrorComponent
                | ApiV1HostsListResourceDiskErrorComponent
                | ApiV1HostsListResourceMemoryErrorComponent
                | ApiV1HostsListRoleErrorComponent
                | ApiV1HostsListScopeErrorComponent
                | ApiV1HostsListSearchErrorComponent
                | ApiV1HostsListStateErrorComponent
                | ApiV1HostsListStateNotErrorComponent
                | ApiV1HostsListTimeRangeErrorComponent
                | ApiV1HostsListUpdatedAtErrorComponent
                | ApiV1HostsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_0 = ApiV1HostsListSearchErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_1 = ApiV1HostsListTimeRangeErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_2 = (
                        ApiV1HostsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_3 = ApiV1HostsListWorkspacesErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_4 = ApiV1HostsListStateErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_hosts_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_5 = ApiV1HostsListKindErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_hosts_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_6 = (
                        ApiV1HostsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_7 = (
                        ApiV1HostsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_8 = ApiV1HostsListNameErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_hosts_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_9 = ApiV1HostsListCreatedAtErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_10 = ApiV1HostsListUpdatedAtErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_11 = ApiV1HostsListScopeErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_12 = ApiV1HostsListProviderErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_13 = (
                        ApiV1HostsListResourceCpuCoresErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_14 = (
                        ApiV1HostsListResourceCpuTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_15 = (
                        ApiV1HostsListResourceCpuArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_16 = (
                        ApiV1HostsListResourceMemoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_17 = (
                        ApiV1HostsListResourceDiskErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_18 = ApiV1HostsListHostnameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_19 = (
                        ApiV1HostsListProviderTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_20 = (
                        ApiV1HostsListProviderImageOsFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_21 = (
                        ApiV1HostsListProviderImageOsVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_22 = (
                        ApiV1HostsListProviderImageOsArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_23 = (
                        ApiV1HostsListProviderDatacenterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_24 = (
                        ApiV1HostsListMaintenancesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_25 = ApiV1HostsListIncidentsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_26 = ApiV1HostsListRoleErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_hosts_list_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_27 = (
                        ApiV1HostsListBootstrapStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_28 = (
                        ApiV1HostsListProviderAccountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_list_error_type_29 = ApiV1HostsListStateNotErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_list_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_hosts_list_error_type_30 = ApiV1HostsListNameExactErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_hosts_list_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_hosts_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_hosts_list_validation_error.additional_properties = d
        return api_v1_hosts_list_validation_error

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
