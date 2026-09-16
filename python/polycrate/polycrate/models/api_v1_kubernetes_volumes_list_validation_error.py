from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_volumes_list_cloud_provider_volume_id_error_component import (
        ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_created_at_error_component import (
        ApiV1KubernetesVolumesListCreatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_created_by_component_error_component import (
        ApiV1KubernetesVolumesListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_created_by_users_error_component import (
        ApiV1KubernetesVolumesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_csi_driver_error_component import (
        ApiV1KubernetesVolumesListCsiDriverErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_incidents_error_component import (
        ApiV1KubernetesVolumesListIncidentsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_k8s_app_error_component import (
        ApiV1KubernetesVolumesListK8SAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_k8s_cluster_error_component import (
        ApiV1KubernetesVolumesListK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_kind_error_component import (
        ApiV1KubernetesVolumesListKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_maintenances_error_component import (
        ApiV1KubernetesVolumesListMaintenancesErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_name_error_component import (
        ApiV1KubernetesVolumesListNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_name_exact_error_component import (
        ApiV1KubernetesVolumesListNameExactErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_organizations_error_component import (
        ApiV1KubernetesVolumesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_phase_error_component import (
        ApiV1KubernetesVolumesListPhaseErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_scope_error_component import (
        ApiV1KubernetesVolumesListScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_search_error_component import (
        ApiV1KubernetesVolumesListSearchErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_state_error_component import (
        ApiV1KubernetesVolumesListStateErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_state_not_error_component import (
        ApiV1KubernetesVolumesListStateNotErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_storage_class_error_component import (
        ApiV1KubernetesVolumesListStorageClassErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_time_range_error_component import (
        ApiV1KubernetesVolumesListTimeRangeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_updated_at_error_component import (
        ApiV1KubernetesVolumesListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_list_workspaces_error_component import (
        ApiV1KubernetesVolumesListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesVolumesListValidationError")


@_attrs_define
class ApiV1KubernetesVolumesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponent |
            ApiV1KubernetesVolumesListCreatedAtErrorComponent | ApiV1KubernetesVolumesListCreatedByComponentErrorComponent |
            ApiV1KubernetesVolumesListCreatedByUsersErrorComponent | ApiV1KubernetesVolumesListCsiDriverErrorComponent |
            ApiV1KubernetesVolumesListIncidentsErrorComponent | ApiV1KubernetesVolumesListK8SAppErrorComponent |
            ApiV1KubernetesVolumesListK8SClusterErrorComponent | ApiV1KubernetesVolumesListKindErrorComponent |
            ApiV1KubernetesVolumesListMaintenancesErrorComponent | ApiV1KubernetesVolumesListNameErrorComponent |
            ApiV1KubernetesVolumesListNameExactErrorComponent | ApiV1KubernetesVolumesListOrganizationsErrorComponent |
            ApiV1KubernetesVolumesListPhaseErrorComponent | ApiV1KubernetesVolumesListScopeErrorComponent |
            ApiV1KubernetesVolumesListSearchErrorComponent | ApiV1KubernetesVolumesListStateErrorComponent |
            ApiV1KubernetesVolumesListStateNotErrorComponent | ApiV1KubernetesVolumesListStorageClassErrorComponent |
            ApiV1KubernetesVolumesListTimeRangeErrorComponent | ApiV1KubernetesVolumesListUpdatedAtErrorComponent |
            ApiV1KubernetesVolumesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponent
        | ApiV1KubernetesVolumesListCreatedAtErrorComponent
        | ApiV1KubernetesVolumesListCreatedByComponentErrorComponent
        | ApiV1KubernetesVolumesListCreatedByUsersErrorComponent
        | ApiV1KubernetesVolumesListCsiDriverErrorComponent
        | ApiV1KubernetesVolumesListIncidentsErrorComponent
        | ApiV1KubernetesVolumesListK8SAppErrorComponent
        | ApiV1KubernetesVolumesListK8SClusterErrorComponent
        | ApiV1KubernetesVolumesListKindErrorComponent
        | ApiV1KubernetesVolumesListMaintenancesErrorComponent
        | ApiV1KubernetesVolumesListNameErrorComponent
        | ApiV1KubernetesVolumesListNameExactErrorComponent
        | ApiV1KubernetesVolumesListOrganizationsErrorComponent
        | ApiV1KubernetesVolumesListPhaseErrorComponent
        | ApiV1KubernetesVolumesListScopeErrorComponent
        | ApiV1KubernetesVolumesListSearchErrorComponent
        | ApiV1KubernetesVolumesListStateErrorComponent
        | ApiV1KubernetesVolumesListStateNotErrorComponent
        | ApiV1KubernetesVolumesListStorageClassErrorComponent
        | ApiV1KubernetesVolumesListTimeRangeErrorComponent
        | ApiV1KubernetesVolumesListUpdatedAtErrorComponent
        | ApiV1KubernetesVolumesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_volumes_list_cloud_provider_volume_id_error_component import (
            ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_created_at_error_component import (
            ApiV1KubernetesVolumesListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_created_by_component_error_component import (
            ApiV1KubernetesVolumesListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_created_by_users_error_component import (
            ApiV1KubernetesVolumesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_csi_driver_error_component import (
            ApiV1KubernetesVolumesListCsiDriverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_incidents_error_component import (
            ApiV1KubernetesVolumesListIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_k8s_app_error_component import (
            ApiV1KubernetesVolumesListK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_k8s_cluster_error_component import (
            ApiV1KubernetesVolumesListK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_kind_error_component import (
            ApiV1KubernetesVolumesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_maintenances_error_component import (
            ApiV1KubernetesVolumesListMaintenancesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_name_error_component import (
            ApiV1KubernetesVolumesListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_organizations_error_component import (
            ApiV1KubernetesVolumesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_phase_error_component import (
            ApiV1KubernetesVolumesListPhaseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_scope_error_component import (
            ApiV1KubernetesVolumesListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_search_error_component import (
            ApiV1KubernetesVolumesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_state_error_component import (
            ApiV1KubernetesVolumesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_state_not_error_component import (
            ApiV1KubernetesVolumesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_storage_class_error_component import (
            ApiV1KubernetesVolumesListStorageClassErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_time_range_error_component import (
            ApiV1KubernetesVolumesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_updated_at_error_component import (
            ApiV1KubernetesVolumesListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_workspaces_error_component import (
            ApiV1KubernetesVolumesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesVolumesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListPhaseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListMaintenancesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListIncidentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListCsiDriverErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesListStateNotErrorComponent):
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
        from ..models.api_v1_kubernetes_volumes_list_cloud_provider_volume_id_error_component import (
            ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_created_at_error_component import (
            ApiV1KubernetesVolumesListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_created_by_component_error_component import (
            ApiV1KubernetesVolumesListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_created_by_users_error_component import (
            ApiV1KubernetesVolumesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_csi_driver_error_component import (
            ApiV1KubernetesVolumesListCsiDriverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_incidents_error_component import (
            ApiV1KubernetesVolumesListIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_k8s_app_error_component import (
            ApiV1KubernetesVolumesListK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_k8s_cluster_error_component import (
            ApiV1KubernetesVolumesListK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_kind_error_component import (
            ApiV1KubernetesVolumesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_maintenances_error_component import (
            ApiV1KubernetesVolumesListMaintenancesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_name_error_component import (
            ApiV1KubernetesVolumesListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_name_exact_error_component import (
            ApiV1KubernetesVolumesListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_organizations_error_component import (
            ApiV1KubernetesVolumesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_phase_error_component import (
            ApiV1KubernetesVolumesListPhaseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_scope_error_component import (
            ApiV1KubernetesVolumesListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_search_error_component import (
            ApiV1KubernetesVolumesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_state_error_component import (
            ApiV1KubernetesVolumesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_state_not_error_component import (
            ApiV1KubernetesVolumesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_storage_class_error_component import (
            ApiV1KubernetesVolumesListStorageClassErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_time_range_error_component import (
            ApiV1KubernetesVolumesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_updated_at_error_component import (
            ApiV1KubernetesVolumesListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_list_workspaces_error_component import (
            ApiV1KubernetesVolumesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponent
                | ApiV1KubernetesVolumesListCreatedAtErrorComponent
                | ApiV1KubernetesVolumesListCreatedByComponentErrorComponent
                | ApiV1KubernetesVolumesListCreatedByUsersErrorComponent
                | ApiV1KubernetesVolumesListCsiDriverErrorComponent
                | ApiV1KubernetesVolumesListIncidentsErrorComponent
                | ApiV1KubernetesVolumesListK8SAppErrorComponent
                | ApiV1KubernetesVolumesListK8SClusterErrorComponent
                | ApiV1KubernetesVolumesListKindErrorComponent
                | ApiV1KubernetesVolumesListMaintenancesErrorComponent
                | ApiV1KubernetesVolumesListNameErrorComponent
                | ApiV1KubernetesVolumesListNameExactErrorComponent
                | ApiV1KubernetesVolumesListOrganizationsErrorComponent
                | ApiV1KubernetesVolumesListPhaseErrorComponent
                | ApiV1KubernetesVolumesListScopeErrorComponent
                | ApiV1KubernetesVolumesListSearchErrorComponent
                | ApiV1KubernetesVolumesListStateErrorComponent
                | ApiV1KubernetesVolumesListStateNotErrorComponent
                | ApiV1KubernetesVolumesListStorageClassErrorComponent
                | ApiV1KubernetesVolumesListTimeRangeErrorComponent
                | ApiV1KubernetesVolumesListUpdatedAtErrorComponent
                | ApiV1KubernetesVolumesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_0 = (
                        ApiV1KubernetesVolumesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_1 = (
                        ApiV1KubernetesVolumesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_2 = (
                        ApiV1KubernetesVolumesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_3 = (
                        ApiV1KubernetesVolumesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_4 = (
                        ApiV1KubernetesVolumesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_5 = (
                        ApiV1KubernetesVolumesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_6 = (
                        ApiV1KubernetesVolumesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_7 = (
                        ApiV1KubernetesVolumesListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_8 = (
                        ApiV1KubernetesVolumesListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_9 = (
                        ApiV1KubernetesVolumesListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_10 = (
                        ApiV1KubernetesVolumesListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_11 = (
                        ApiV1KubernetesVolumesListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_12 = (
                        ApiV1KubernetesVolumesListK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_13 = (
                        ApiV1KubernetesVolumesListK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_14 = (
                        ApiV1KubernetesVolumesListPhaseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_15 = (
                        ApiV1KubernetesVolumesListStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_16 = (
                        ApiV1KubernetesVolumesListMaintenancesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_17 = (
                        ApiV1KubernetesVolumesListIncidentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_18 = (
                        ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_19 = (
                        ApiV1KubernetesVolumesListCsiDriverErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_list_error_type_20 = (
                        ApiV1KubernetesVolumesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_list_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_volumes_list_error_type_21 = (
                    ApiV1KubernetesVolumesListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_volumes_list_error_type_21

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_volumes_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_volumes_list_validation_error.additional_properties = d
        return api_v1_kubernetes_volumes_list_validation_error

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
